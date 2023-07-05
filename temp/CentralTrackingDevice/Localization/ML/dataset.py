import cv2
import numpy as np
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)

cap = cv2.VideoCapture(3)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

curr_x = 400
curr_y = 70 + 50
while True:
    ret, img = cap.read()
    print(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    res = cv2.aruco.detectMarkers(gray, dictionary)
    if res is not None:
        if 83 in res[1]:
            index = np.where(res[1] == 83)[0][0]
            x1 = (res[0][index][0][0][0] + res[0][index][0][2][0])//2
            y1 = (res[0][index][0][0][1] + res[0][index][0][2][1])//2
            cv2.circle(img, (int(x1), int(y1)), 10, (0, 0, 255), -1)
    cv2.imshow("asd.png", img)
    if cv2.waitKey(25) & 0xFF == ord('s'):
        with open('r.txt', 'a') as fd:
            fd.write(f"{curr_x} {curr_y} {x1} {y1}")
            fd.write('\n')
        curr_x += 50
        if curr_x >= 2800:
            curr_x = 200
            curr_y += 50
        if curr_y >= 2000:
            print("Finish")
