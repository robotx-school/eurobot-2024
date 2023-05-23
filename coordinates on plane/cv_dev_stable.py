import cv2
import numpy as np
import torch
from torch import nn, optim
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self,neyrons):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(2, 10)
        self.fc2 = nn.Linear(10, 100)
        self.fc3 = nn.Linear(100, 150)
        self.fc4 = nn.Linear(150, 100)
        self.fc5 = nn.Linear(100, 10)
        self.fc6 = nn.Linear(10, 2)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        x = F.relu(self.fc5(x))
        x = self.fc6(x)
        return x


hand = [0,0]
savescreen = False
get_aruco = [141, 142, 139, 140]

with open('lib.cv') as f:
    K = eval(f.readline())
    D = eval(f.readline())

def undistort(img):
    DIM = img.shape[:2][::-1]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    return undistorted_img[::]

x_cord = [0,0,0,0]
y_cord = [0,0,0,0]
middles = [0,0,0,0]

field = np.zeros((4000, 3000,3), dtype='uint8')
cv2.rectangle(field, (500,500), (2500,3500), (0, 255, 0), 2)

is_working = True
camport=1
q=False

DEVICE = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
net = torch.load('model.t')
net.eval()
        
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)

while(True):
    while is_working:
        cap = cv2.VideoCapture(camport,cv2.CAP_DSHOW)
        
        cap.set(3,1920)
        cap.set(4,1080)
        cap.set(30, 0.1)
        
        if not cap.isOpened():
            print("USB port - not found")
        else:
            is_working = False
    _,img = cap.read()
    img = undistort(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    res = cv2.aruco.detectMarkers(gray,dictionary)
    height, width, _ = img.shape
    if res[1] is not None:
    
        kubs = [132, 133, 134, 135]
        if kubs[0] in res[1] or kubs[1] in res[1] or kubs[2] in res[1] or kubs[3] in res[1]:
            for a in range(4):
                index = np.where(res[1] == list(set(np.ravel(res[1])) & set(kubs)))[0][0]
                x_middle=0
                y_middle=0
                coords = []
                coords.append([int(res[0][index][0][0][0]),int(res[0][index][0][0][1])])
                x_test = torch.Tensor([[int(res[0][index][0][0][0]), int(res[0][index][0][0][1])]])/3000
                x_test.unsqueeze_(1)
                x_test = x_test.to(DEVICE)
                y_pred = net.forward(x_test)*3000
                print(int(y_pred))
                cv2.circle(field, (int(y_pred[0][0][0])+500,int(y_pred[0][0][1])+500), 5, (0,0,255), -1)
                middles[a] = [int(res[0][index][0][0][0]),int(res[0][index][0][0][1])]
                
         
                
                
            
            middles[0][0] = middles[0][0] + 360 + 170 + 150 + 35 - 10 - 100 
            middles[0][1] = middles[0][1] + 310 + 50 + 100 - 245 - 200
            
            middles[1][0] = middles[1][0] - 290 - 100 - 150 - 25
            middles[1][1] = middles[1][1] + 270 + 88 -50 - 205
            
            middles[2][0] = middles[2][0] - 70 +35-40-35 - 30 + 15 
            middles[2][1] = middles[2][1] - 100 - 147+7

            middles[3][0] = middles[3][0] + 80 + 5 + 40  + 23
            middles[3][1] = middles[3][1] - 100 - 135 - 20
            

            #print(net(middles[0][0],middles[0][1])################ 
            input_pt = np.array(middles)
            output_pt = np.array([[0, 0], [width, 0],[width, height],[0, height]])
            h, _ = cv2.findHomography(input_pt, output_pt)
            res_img = cv2.warpPerspective(img, h, (width, height))



            gray_aruco = cv2.cvtColor(res_img, cv2.COLOR_BGR2GRAY)

            res_aruco = cv2.aruco.detectMarkers(gray_aruco,dictionary)
            

    cv2.imshow('img1',img)
    field = cv2.resize(field, (375, 500))
    cv2.imshow('field', field)
    print
    
    if savescreen == False:
        if cv2.waitKey(1) & 0xFF == ord('y'):

            q=True
            cv2.destroyAllWindows()
            print("Screen saved!")
            break





cap.release()
