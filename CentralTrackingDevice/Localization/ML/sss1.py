import cv2

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
#ret,frame = cap.read() # return a single frame in variable `frame`


def coord_gen():
    for i in range(700, 2700, 100):
        for j in range(0, 1700, 100):
            yield (i,j)

    
coord = coord_gen()  
while(True):
    
    print(next(coord))
