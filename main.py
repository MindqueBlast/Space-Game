# Import the pygame module
import pygame

# Import pygame.locals for easier access to key coordinates
from pygame.locals import *
from pygame import mixer

# Initialize pygame
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg = pygame.image.load("assets/background.png")
bg = pygame.transform.scale(bg,(SCREEN_WIDTH, SCREEN_HEIGHT))

mixer.init()
mixer.music.load('assets/Sounds/music.wav')
mixer.music.play()
# Main loop
runing = True
while runing:
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            runing = False
    pygame.display.update()
pygame.quit()