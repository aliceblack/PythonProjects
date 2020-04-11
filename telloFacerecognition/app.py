import numpy as np
import cv2
import time
import pygame
import numpy
import sys

if len(sys.argv) > 1:
    if sys.argv[1] == 'debug':
        print('Starting in debug mode...')
        import commandsMock as droneCommands
    else:
        import commands as droneCommands
else:
        import commands as droneCommands


pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame OpenCV face recognition')
white = (255,255,255)
text = pygame.font.Font(None, 45)


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def droneFaceRec():
    continueView = True
    droneCommands.streamOn()
    cam = droneCommands.videoCapture()
    while continueView:
        frame = None
        ret_val, frame = cam.read()
        if not(ret_val):
            cam = droneCommands.videoCapture()
            ret_val, frame = cam.read()
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
        frame = numpy.rot90(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = pygame.surfarray.make_surface(frame)
        screen.blit(frame, (0,0))
        if len(faces)>0:
            if len(faces[0])>0:
                label = text.render("x -> "+str(faces[0][0]), 1, white)
                screen.blit(label, (420, 410))
                label = text.render("y -> "+str(faces[0][1]), 1, white)
                screen.blit(label, (400, 410))
                x = faces[0][0]
                y = faces[0][1]
                if x<100:
                    label = text.render("Too right", 1, white)
                    screen.blit(label, (400, 430))
                    droneCommands.left()
                if x>700:
                    lael = text.render("Too left", 1, white)
                    screen.blit(label, (400, 430))
                    droneCommands.right()
                if y<10:
                    label = text.render("Too high", 1, white)
                    screen.blit(label, (400, 430))
                    droneCommands.down()
                if y>400:
                    label = text.render("Too low", 1, white)
                    screen.blit(label, (400, 430))
                    droneCommands.up()
        pygame.display.update()
        #Keyboard mapping
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    continueView=False


continueGame = True
while continueGame:
    # press esc to quit
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    continueGame=False
                elif event.key == pygame.K_o:
                    droneCommands.command()
                elif event.key == pygame.K_p:
                    droneCommands.takeoff()
                elif event.key == pygame.K_v:
                    droneFaceRec()    
                break 