import cv2
import numpy as np
import os
import glob
import torch
from torch import nn, optim
import torch.nn.functional as F
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)

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
img = cv2.imread('test.png')
with open('cords.txt','w') as f:
    final_str = ""
    gray = cv2.cvtcolor(img, cv2.color_bgr2gray)
    res = cv2.aruco.detectMarkers(gray,dictionary)
    
    if res is not None:
        if 135 in res[1]:
            index = np.where(res[1] == 135)[0][0]
            x1 = (res[0][index][0][0][0] + res[0][index][0][2][0])//2
            y1 = (res[0][index][0][0][1] + res[0][index][0][2][1])//2
            cv2.circle(img, (int(x1),int(y1)), 10, (0,0,255), -1)
            b=img.split('_')
            x=b[0][1:]
            y=b[1].split('.')[0][1:]
            print(net([[x1,y1]]))
            #ff = str(int(x1))+' '+str(int(y1))+' '+str(int(float(x)))+' '+str(int(float(y)))
            #final_str += f"{ff}\n"
            #print("OK")
f.write(final_str)
