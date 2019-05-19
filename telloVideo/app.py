import sys
from datetime import datetime
import time
import pygame
import cv2 as cv
import numpy
import commands as droneCommands


#Screen and controls
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Cockpit')

text = pygame.font.Font(None,25)
white = (255,255,255)

def showKeyBindings():
    labelParagraph = text.render("Key bindings", 1, white)
    screen.blit(labelParagraph, (100, 100))

    labelExit = text.render("Esc - exit", 1, white)
    screen.blit(labelExit, (200, 200))

    labelStart = text.render("O - start", 1, white)
    screen.blit(labelStart, (200, 230))

    labelTakeoff = text.render("P - takeoff", 1, white)
    screen.blit(labelTakeoff, (200, 260))

    labelLand = text.render("H - land", 1, white)
    screen.blit(labelLand, (200, 290))

    label = text.render("W A S D", 1, white)
    screen.blit(label, (400, 200))

    label = text.render("Up Down Left Right", 1, white)
    screen.blit(label, (400, 230))

    label = text.render("Flip - I J K L", 1, white)
    screen.blit(label, (400, 260))

    label = text.render("V - video streaming ", 1, white)
    screen.blit(label, (400, 290))

#Show key bindings
showKeyBindings()
pygame.display.update()


def showDroneView():
    continueView = True
    droneCommands.streamOn()
    cam = droneCommands.videoCapture()
    while continueView:
        #Webcam feed
        ret_val, frame = cam.read()
        #Set correct colors
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        #Set correct rotation
        frame = numpy.rot90(frame)
        #Set pygame surface
        frame = pygame.surfarray.make_surface(frame)
        screen.blit(frame, (0,0))
        showKeyBindings()
        pygame.display.update()
        #Keyboard mapping
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    continueView=False #Exit using esc
                elif event.key == pygame.K_p:
                    droneCommands.takeoff()
                elif event.key == pygame.K_h:
                    droneCommands.land()
                elif event.key == pygame.K_w:
                    droneCommands.forward()
                elif event.key == pygame.K_s:
                    droneCommands.back()
                elif event.key == pygame.K_a:
                    droneCommands.couterClockwise()
                elif event.key == pygame.K_d:
                    droneCommands.clockWise()
                elif event.key == pygame.K_UP:
                    droneCommands.up()
                elif event.key == pygame.K_DOWN:
                    droneCommands.down()
                elif event.key == pygame.K_LEFT:
                    droneCommands.left()
                elif event.key == pygame.K_RIGHT:
                    droneCommands.right()
                elif event.key == pygame.K_i:
                    droneCommands.flipForward()
                elif event.key == pygame.K_k:
                    droneCommands.flipBack
                elif event.key == pygame.K_j:
                    droneCommands.flipLeft()
                elif event.key == pygame.K_l:
                    droneCommands.flipRight()
                break

#listen for first commands
continueGame = True
while continueGame:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continueGame=False
            elif event.key == pygame.K_v:
                showDroneView()
            elif event.key == pygame.K_o:
                droneCommands.command()
            break



print("flight ended")


