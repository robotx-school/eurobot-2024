import torch
import cv2
import numpy as np
import torch
from torch import nn, optim
import torch.nn.functional as F


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

net = torch.load("model.t")
net = net.to(torch.device("cuda"))
img = cv2.imread('photo_2023-05-30_16-52-19.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
res = cv2.aruco.detectMarkers(gray,dictionary)
if res is not None:
    if 135 in res[1]:
        index = np.where(res[1] == 135)[0][0]
        x1 = (res[0][index][0][0][0] + res[0][index][0][2][0])//2
        y1 = (res[0][index][0][0][1] + res[0][index][0][2][1])//2
        cv2.circle(img, (int(x1), int(y1)), 10, (0, 0, 255), -1)
        #b = img.split('_')
        #x = b[0][1:]
        #y = b[1].split('.')[0][1:]


x_test = torch.Tensor([[x1, y1]]) / 3000
x_test.unsqueeze_(1)
x_test = x_test.to(torch.device("cuda"))
y_pred = net.forward(x_test)*3000

y_pred = list(y_pred.detach().cpu().numpy())
print(y_pred)

