import cv2 as cv
import time
import pygame
import numpy

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame OpenCV stream')



def show_webcam():
    continueGame = True
    cam = cv.VideoCapture(0)
    while continueGame:
        #Webcam feed
        ret_val, frame = cam.read()
        #Set correct colors
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        #Set correct rotation
        frame = numpy.rot90(frame)
        #Set pygame surface
        frame = pygame.surfarray.make_surface(frame)
        screen.blit(frame, (0,0))
        pygame.display.update()
        #Keyboard mapping
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print("key pression")
                #Exit using esc
                if event.key == pygame.K_ESCAPE:
                    continueGame=False
                break

def main():
    show_webcam()

print('OpenCV camera stream on Pygame and listens for key pression')
print("Press Esc to quit")
main()

