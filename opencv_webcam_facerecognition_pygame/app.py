import numpy as np
import cv2
import time
import pygame
import numpy

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame OpenCV face recognition')
white = (255,255,255)
text = pygame.font.Font(None, 25)


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)
continueGame = True
while continueGame:
    ret_val, frame = cam.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        # frame  = cv2.putText(frame, "x  "+str(x)+"  |  y "+str(y), (x, y), cv2.FONT_HERSHEY_SIMPLEX, .5,(255,255,255),2,cv2.LINE_AA)
    frame = numpy.rot90(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = pygame.surfarray.make_surface(frame)
    screen.blit(frame, (0,0))
    if len(faces)>0:
        if len(faces[0])>0:
            label = text.render("x -> "+str(faces[0][0]), 1, white)
            screen.blit(label, (400, 410))
            x = faces[0][0]
            y = faces[0][1]
            if x<100:
                label = text.render("Too right", 1, white)
                screen.blit(label, (400, 430))
            if x>400:
                label = text.render("Too left", 1, white)
                screen.blit(label, (400, 430))
            if y<50:
                label = text.render("Too high", 1, white)
                screen.blit(label, (400, 430))
            if y>240:
                label = text.render("Too low", 1, white)
                screen.blit(label, (400, 430))
    pygame.display.update()
    # press esc to quit
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print("key pression")
                #Exit using esc
                if event.key == pygame.K_ESCAPE:
                    continueGame=False
                break 