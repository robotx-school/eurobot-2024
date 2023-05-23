import cv2
import numpy as np
with open('e.txt') as f:
    K = eval(f.readline())
    D = eval(f.readline())

def undistort(img):
    DIM = img.shape[:2][::-1]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    return undistorted_img[::]





def coord_gen():
    for i in range(2700, 700, -100):
        for j in range(0, 1700, 100):
            yield (j,i)


cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
cap.set(3,1920)
cap.set(4,1080)
cap.set(30, 0.1)
# video capture source camera (Here webcam of laptop) 
#ret,frame = cap.read() # return a single frame in variable `frame`
coord = coord_gen()
x, y = next(coord)
while(True):
    
    ret,frame = cap.read()
    frame = undistort(frame)
    cv2.putText(frame, f"change robot to coords: {x}, {y}",
                        (200,200),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0,255,0), 2, cv2.LINE_AA)
    cv2.imshow('img1',frame)
    if cv2.waitKey(50) == 32:
        cv2.imwrite(f'x{x+11.5}_y{y+11.5}.png',frame)
        x, y = next(coord)
    print(x, y)
cap.release()
