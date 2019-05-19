from tello import Tello
import sys
from datetime import datetime
import time
import pygame
import cv2 as cv

#Screen and controls
pygame.init()

#Show key bindings
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Cockpit')

text = pygame.font.Font(None,25)
white = (255,255,255)

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

pygame.display.update()

#Initialize drone
tello = Tello()

#Keyboard mappings
continueGame = True
while continueGame:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continueGame=False
            elif event.key == pygame.K_o:
                tello.send_command('command')
            elif event.key == pygame.K_p:
                tello.send_command('takeoff')
            elif event.key == pygame.K_h:
                tello.send_command('land')
            elif event.key == pygame.K_w:
                tello.send_command('forward 40')
            elif event.key == pygame.K_s:
                tello.send_command('back 40')
            elif event.key == pygame.K_a:
                tello.send_command('ccw 45')
            elif event.key == pygame.K_d:
                tello.send_command('cw 45')
            elif event.key == pygame.K_UP:
                tello.send_command('up 40')
            elif event.key == pygame.K_DOWN:
                tello.send_command('down 40')
            elif event.key == pygame.K_LEFT:
                tello.send_command('left 40')
            elif event.key == pygame.K_RIGHT:
                tello.send_command('right 40')
            elif event.key == pygame.K_i:
                tello.send_command('flip f')
            elif event.key == pygame.K_k:
                tello.send_command('flip b')
            elif event.key == pygame.K_j:
                tello.send_command('flip l')
            elif event.key == pygame.K_l:
                tello.send_command('flip r')
            elif event.key == pygame.K_v:
                tello.send_command('streamon')   
                cam = cv.VideoCapture('udp://@0.0.0.0:11111')
                while True:
                    ret_val, frame = cam.read()
                    cv.imshow('Drone feed', frame)
                    # press esc to quit #cv will block pygame keyboard bindings
                    if cv.waitKey(1) == 27: 
                        break  
                # release
                cv.destroyAllWindows() 
            break

print("end")