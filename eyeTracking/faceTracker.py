import time
import cv2 
import numpy as np
import serial

arduino_data = serial.Serial('/dev/cu.usbmodem1411', 9600, timeout=1)


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')
eye_cascade =   cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

blink = False 
ui = '1'
while True:
	ui = input('enter: ')
	if ui=='q':
		break
	else:
		arduino_data.write(ui.encode('utf-8'))

	

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces: # detect face
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2) # draw rect
        blink = True
        for (q,a,c,v) in eyes: # user blinks if program no longer detects eye
            blink = False
            cv2.rectangle(frame, (q,a), (q+c, a+v), (255,0,0), 2) # draw rect

    cv2.imshow('frame', frame)
            
    while blink==True: # while user blinking
        time.sleep(0.3)
        if(blink==True): # account for glitchy detection
            arduino_data.write(ui.encode('utf-8')) # send serial to actuate servo
            blink=False


    
    
    if cv2.waitKey(1) & 0xFF == ord('r'):
        break

        cap.release()
        cv2.destroyAllWindows()


