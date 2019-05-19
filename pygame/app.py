import time
import pygame

pygame.init()

#Create game window in order to get keyboard input
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame keyboard')


continueGame = True

while continueGame:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print("pression")
            if event.key == pygame.K_ESCAPE:
                continueGame=False
            break

print("end")