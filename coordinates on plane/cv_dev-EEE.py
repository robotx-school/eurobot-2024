import cv2
import numpy as np
import torch
from torch import nn, optim
import torch.nn.functional as F
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


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


net = torch.load('model.t')


hand = [0,0]
savescreen = False
get_aruco = [141, 142, 139, 140]
path = "C:\\Users\\Stepan\\Desktop\\08-11\\plane.png"
plane_path = cv2.imread(path, cv2.IMREAD_COLOR)
plane_path_raws, plane_path_cols, plane_path_ch = plane_path.shape
def plane_show(x, y):
    plane_path_copy = plane_path.copy()
    plane_path_copy = cv2.resize(plane_path_copy, (3000, 2000))
    cv2.circle(plane_path_copy, (x, y), 0, (0, 0, 255), 150)
    plane_path_copy = cv2.resize(plane_path_copy, (450, 300))
    cv2.imshow('plane', plane_path_copy)
    cv2.waitKey(1)

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

is_working = True
camport=1
q=False

        
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)


while(True):
    while is_working:
        cap = cv2.VideoCapture(camport,cv2.CAP_DSHOW)
        
        cap.set(3,1920)
        cap.set(4,1080)
        cap.set(30, 0.1)
        
    #n
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
    
        kubs = [20,21,23,22]
        if kubs[0] in res[1] and kubs[1] in res[1] and kubs[2] in res[1] and kubs[3] in res[1]:

            for a in range(4):
                index = np.where(res[1] == kubs[a])[0][0]
                
                x_middle=0
                y_middle=0
                coords = []
                
                for i in range(4):
                    coords.append([int(res[0][index][0][i][0]),int(res[0][index][0][i][1])])
                    x_cord[i]=int(res[0][index][0][i][0])
                    y_cord[i]=int(res[0][index][0][i][1])
                    #cv2.circle(img, (x_cord[i],y_cord[i]), 5, (0,0,255), -1)
                    if a == i:
                        middles[a] = [x_cord[i], y_cord[i]]
                
 
                
                
            #print(middles)
            
            middles[0][0] = middles[0][0] + 360 + 170 + 150 + 35 - 10 - 100 #bottom left
            middles[0][1] = middles[0][1] + 310 + 50 + 100 - 245 - 200
            #print("bottom left:", middles[0][0], middles[0][1])
            
            middles[1][0] = middles[1][0] - 290 - 100 - 150 - 25# uper left
            middles[1][1] = middles[1][1] + 270 + 88 -50 - 205
            
            #print("uper left:", middles[1][0], middles[1][1])
            
            middles[2][0] = middles[2][0] - 70 +35-40-35 - 30 + 15 # upper right
            middles[2][1] = middles[2][1] - 100 - 147+7
            #print("upper right:", middles[2][0], middles[2][1])

            middles[3][0] = middles[3][0] + 80 + 5 + 40  + 23# bottom right
            middles[3][1] = middles[3][1] - 100 - 135 - 20 #+ 15 
            #print("bottom right:", middles[3][0], middles[3][1])
            

                
            input_pt = np.array(middles)
            output_pt = np.array([[0, 0], [width, 0],[width, height],[0, height]])
            h, _ = cv2.findHomography(input_pt, output_pt)
            res_img = cv2.warpPerspective(img, h, (width, height))
            print('cooooords',net([[x_middle,y_middle]]))


            #gray_aruco = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #Edit 01.11.2022/17.29
            gray_aruco = cv2.cvtColor(res_img, cv2.COLOR_BGR2GRAY)

            res_aruco = cv2.aruco.detectMarkers(gray_aruco,dictionary)
            for marker in get_aruco:
                if marker in res_aruco[1]:
                    #print(11111, marker)
                    #print(222222,res_aruco[1])
                    index = np.where(res_aruco[1] == marker)[0][0]
                    #print(333333,index)
                    pt0 = res_aruco[0][index][0][0].astype(np.int16)
                    #coords.append(list(pt0))
                    print("arUco:", marker, "("+str(index)+")", "|", "Cords on image:", "X", list(pt0)[0], "/", "Y", list(pt0)[1], "|", "Real cords:", "X", str(int((list(pt0)[1])*2.7)+170), "Y", str(int((list(pt0)[0])*1.05)), "|","Max image cords:", res_img.shape[1], "/", res_img.shape[0])
                    plane_show(int(str(int((list(pt0)[1])*2.7)+170)), 2000-int(str(int((list(pt0)[0])*1.05))))
            #print(res_aruco[0])
            cv2.imshow('b',cv2.rotate(cv2.rotate(cv2.resize(res_img, (2340//3, 3550//3)), cv2.cv2.ROTATE_180), cv2.cv2.ROTATE_90_CLOCKWISE))
        
    #cv2.imshow('img1',cv2.resize(img, (1080//2, 1080//2)))
    cv2.imshow('img1',img)
    #display the captured image
    if savescreen == False:
        if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y'

            q=True
            cv2.destroyAllWindows()
            print("Screen saved!")
            break





while(q):
    while is_working:
        cap = cv2.VideoCapture(camport,cv2.CAP_DSHOW)
        
        cap.set(3,1920)
        cap.set(4,1080)
        cap.set(30, 0.1)
        
    #n
        if not cap.isOpened():
            print("USB port - not found")
        else:
            is_working = False
    _,img = cap.read()
    img = undistort(img)
    gray_test = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    res_test = cv2.aruco.detectMarkers(gray_test,dictionary)
    res_img = cv2.warpPerspective(img, h, (width, height))
    gray_aruco = cv2.cvtColor(res_img, cv2.COLOR_BGR2GRAY)
    res_aruco = cv2.aruco.detectMarkers(gray_aruco,dictionary)
    for marker in get_aruco:
        if marker in res_aruco[1]:
            #print(11111, marker)
            #print(222222,res_aruco[1])
            index = np.where(res_aruco[1] == marker)[0][0]
            #print(333333,index)
            pt0 = res_aruco[0][index][0][0].astype(np.int16)
            #coords.append(list(pt0))
            print("arUco:", marker, "("+str(index)+")", "|", "Cords on image:", "X", list(pt0)[0], "/", "Y", list(pt0)[1], "|", "Real cords:", "X", str(int((list(pt0)[1])*2.7)+170), "Y", str(int((list(pt0)[0])*1.05)), "|","Max image cords:", res_img.shape[1], "/", res_img.shape[0])
            plane_show(int(str(int((list(pt0)[1])*2.7)+170)), 2000-int(str(int((list(pt0)[0])*1.05))))
    cv2.imshow('b',cv2.rotate(cv2.rotate(cv2.resize(res_img, (2340//3, 3550//3)), cv2.cv2.ROTATE_180), cv2.cv2.ROTATE_90_CLOCKWISE))
    #cv2.imshow('img1',cv2.resize(img, (1080//2, 1080//2)))
    cv2.imshow('img1',img)
    #display the captured image
    if savescreen == False:
        if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y'
            
            cv2.imwrite(f'c{str(i).rjust(5, "-")}.png',frame)

            cv2.destroyAllWindows()
            savescreen = True
            print("Screen saved!")
            break

cap.release()
