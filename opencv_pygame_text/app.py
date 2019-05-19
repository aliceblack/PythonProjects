import cv2 as cv
import time
import pygame
import numpy

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame OpenCV stream')

text = pygame.font.Font('tigedeblug.ttf',25) # otherwise .Font(None, size) or .SysFont('Arial',size)
white = (255,255,255)

#Show text in Pygame window
def showKeyBindings():

    labelExit = text.render("Esc - exit", 1, white)
    screen.blit(labelExit, (50, 410))

    labelStart = text.render("O - start", 1, white)
    screen.blit(labelStart, (50, 430))

    label = text.render("V - video streaming ", 1, white)
    screen.blit(label, (50, 450))

    labelTakeoff = text.render("P - takeoff", 1, white)
    screen.blit(labelTakeoff, (250, 430))

    labelLand = text.render("H - land", 1, white)
    screen.blit(labelLand, (250, 450))

    label = text.render("W A S D", 1, white)
    screen.blit(label, (400, 410))

    label = text.render("Up Down Left Right", 1, white)
    screen.blit(label, (400, 430))

    label = text.render("Flip - I J K L", 1, white)
    screen.blit(label, (400, 450))


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
        showKeyBindings()
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

