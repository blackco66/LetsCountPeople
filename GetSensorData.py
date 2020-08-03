import numpy as np
import imutils
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import requests
import time

Gym_name='Gyminthehous'
time_interval = 10
url_post = 'http://127.0.0.1:8000'

avg = None
xvalues = list()
motion = list()
count1 = 0
count2 = 0
people_num =0 
def find_majority(k):
    myMap={}


    maximum = ('',0) # (occurirng element, occurence)
    for n in k:
        if n in myMap: myMap[n] += 1
        else: myMap[n] = 1

        if myMap[n] > maximum[1]: maximum = (n,myMap[n])
    return maximum   

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate =12 
rawCapture = PiRGBArray(camera, size=(640,480))

time.sleep(0.1)
bf = time.time()
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    
    image_t = frame.array
    text = "Unoccupied"
    image = imutils.resize(image_t, width=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21),0)

    if avg is None:
        print("[info] starting background model....")
        avg = gray.copy().astype("float")
        rawCapture.truncate(0)
        continue


    cv2.accumulateWeighted(gray, avg, 0.5)
    frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))
    thresh = cv2.threshold(frameDelta, 5, 255, cv2.THRESH_BINARY)[1]


    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    flag = True
    for c in cnts:
        if cv2.contourArea(c) < 5000:
            continue
        (x,y,w,h)= cv2.boundingRect(c)
        xvalues.append(x)
        cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255) , 2)
        flag = False

    no_x = len(xvalues)

    if (no_x > 2):
        difference = xvalues[no_x -1] - xvalues[no_x -2]
        if(difference > 0):
            motion.append(1)
        elif(difference <0):
            motion.append(0)

    if flag is True:
        if (no_x > 5):
            val, times = find_majority(motion)
            if val == 1 and times >=4:
                count1 += 1
            else:
                count2 += 1
        xvalues = list()
        motion = list()
    people_num = count1-count2 
    if people_num < 0:
        people_num = 0
        count1 = 0
        count2 = 0 
    af = time.time()
    if af-bf > time_interval:
        print("Posting that {} people in here".format(people_num))
        param = {'gymname' : Gym_name, 'num_people': people_num}
        r=requests.post(url_post,data=param)
        print(r.status_code)
        bf = time.time()

    cv2.line(image, (260,0), (260,480), (0,255,0) ,2)
    cv2.line(image, (420,0), (420,480), (0,255,0) ,2)
    cv2.putText(image, "In: {}".format(count1), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
    cv2.putText(image, "Out  : {}".format(count2), (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
    cv2.imshow("Frame", image)
    #cv2.imshow("Gray", gray)
    #cv2.imshow("FrameDelta", frameDelta)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    rawCapture.truncate(0)


cv2.destroyAllWindows() 


 




