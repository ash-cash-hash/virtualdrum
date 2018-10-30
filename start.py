import numpy as np
import cv2
import imutils
import pygame
cap=cv2.VideoCapture(0)
def playsound1(frame):
    cv2.rectangle(frame,(0,300),(150,470),(255,255,0),2)
    cv2.rectangle(frame,(500,300),(650,470),(0,255,0),2)
    cv2.rectangle(frame,(250,430),(400,470),(255,0,0),2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'welcome to Virtual Drum',(50,70), font, 1,(0,0,0),2)




# print(flag)
def findColor(frame):

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blurred=cv2.GaussianBlur(frame,(11,11),0)
    hsv=cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    lower=np.array([30,100,50])
    upper=np.array([75,255,255])
    mask=cv2.inRange(hsv,lower,upper)
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=2)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    center = None

    # only proceed if at least one contour was found
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        # print(center)
        if radius > 5:
            # print('hello')
            cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
            # print('---',x,y)
            if int(x)<150 & int(y)>300 & flag==0:
                pygame.mixer.init()
                pygame.mixer.music.load("d1.wav")
                pygame.mixer.music.play()
                flag=1

            if int(x)>150 & flag==1:
                print('hello')
                flag=0
            # cv2.circle(frame, center, 5, (0, 0, 255), -1)
    return frame








def findColor1(frame):
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blurred=cv2.GaussianBlur(frame,(11,11),0)
    hsv=cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    # cv2.imshow('window',hsv)
    lower=np.array([0,100,50])
    upper=np.array([30,255,255])
    mask=cv2.inRange(hsv,lower,upper)

    # join my masks

    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=2)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    center = None
    # only proceed if at least one contour was found
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 5:
            # print('hello')
            cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
            # cv2.circle(frame, center, 5, (0, 0, 255), -1)
    return frame






def start():
    flag=0
    flagx=0
    flagt=0
    falgt1=0
    while(True):
        ret, frame=cap.read()
        # gray=cv2.flip(src=gray,flipCode=1)
        frame=cv2.flip(src=frame,flipCode=1)
        print(flag)




        # frame=findColor(frame)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        blurred=cv2.GaussianBlur(frame,(11,11),0)
        hsv=cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        lower=np.array([30,100,50])
        upper=np.array([75,255,255])
        mask=cv2.inRange(hsv,lower,upper)
        mask=cv2.erode(mask,None,iterations=2)
        mask=cv2.dilate(mask,None,iterations=2)
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        center = None

        # only proceed if at least one contour was found
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            # print(center)
            if radius > 20:
                # print('hello')
                cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                print('---',int(x),int(y))
                if int(x)<150 and int(y)>300 and flag==0:
                    pygame.mixer.init()
                    pygame.mixer.music.load("d1.wav")
                    pygame.mixer.music.play()
                    flag=1

                if int(x)>150 and flag==1:
                    print('hello')
                    flag=0
                if 250<int(x)<400 and 430<int(y)<470 and flagt==0:
                    pygame.mixer.init()
                    pygame.mixer.music.load("dx.wav")
                    pygame.mixer.music.play()
                    falgt=1
                if int(y)<430 and flagt==1:
                    flagt=0

        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        blurred=cv2.GaussianBlur(frame,(11,11),0)
        hsv=cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        # cv2.imshow('window',hsv)
        lower=np.array([0,120,90])
        upper=np.array([30,255,255])
        mask=cv2.inRange(hsv,lower,upper)

        # join my masks

        mask=cv2.erode(mask,None,iterations=2)
        mask=cv2.dilate(mask,None,iterations=2)
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        center = None
        # only proceed if at least one contour was found
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            if radius > 20:
                # print('hello')
                cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                print('---',int(x),int(y))
                if int(x)>500 and int(y)>300 and flagx==0:
                    pygame.mixer.init()
                    pygame.mixer.music.load("d3.wav")
                    pygame.mixer.music.play()
                    flagx=1

                if int(x)<500 and flagx==1:
                    print('hello')
                    flagx=0

        # frame=findColor1(frame)
                # pts.appendleft(center)
        playsound1(frame)


                # for i in range(1, len(pts)):
                #     # if either of the tracked points are None, ignore
                #     # them
                #     if pts[i - 1] is None or pts[i] is None:
                #         continue
                #         # otherwise, compute the thickness of the line and
                #         # draw the connecting lines
                #         thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
                #         cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

                        # show the frame to our screen
        cv2.imshow("Frame", frame)

                        #####################



















                        # indices=np.where(mask!=[0])
                        # coordinates=zip(indices[0],indices[1])
                        # output=cv2.bitwise_and(frame,frame,mask=mask)
                        # output=cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)
                        # output=cv2.medianBlur(output,5)
                        # cv2.imshow('window',output)
                        # edge=cv2.Canny(output,100,200)
                        # # cv2.imshow('window',edge)
                        # im2, contours = cv2.findContours(output.copy(),1,2)
                        # # print(contours)
                        # # ret,thresh=cv2.threshold(output,127,255,0)
                        # contours , im2 = cv2.findContours(output.copy(),1,2)
                        # # cv2.drawContours(frame,contours[0], 0, (0,255,0), 3)
                        # x,y,w,h = cv2.boundingRect(contours[0])
                        # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                        # # cv2.imshow("found",edge)
                        #
                        #
                        #
                        #
                        #
                        # cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
                            break
                            cap.release()
                            cv2.destroyAllWindows()

start()
