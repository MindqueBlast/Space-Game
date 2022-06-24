import pygame

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg = pygame.image.load("assets/background.png")
bg = pygame.transform.scale(bg,(SCREEN_WIDTH, SCREEN_HEIGHT))

player_sprite = pygame.image.load("assets/player_sprites/playerShip1_blue.png")
meteor_images = [pygame.image.load("assets/meteors/meteorGrey_big1.png"), pygame.image.load("assets/meteors/meteorGrey_big2.png"), pygame.image.load("assets/meteors/meteorGrey_big3.png"), pygame.image.load("assets/meteors/meteorGrey_big4.png"), pygame.image.load("assets/meteors/meteorBrown_big1.png"), pygame.image.load("assets/meteors/meteorBrown_big2.png"), pygame.image.load("assets/meteors/meteorBrown_big3.png"), pygame.image.load("assets/meteors/meteorBrown_big4.png"),]
bullet_img = pygame.image.load("assets\lasers\laserBlue.png")

meteors = []
bullets = []
