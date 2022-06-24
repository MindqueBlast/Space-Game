# Import the pygame module
import pygame, sys, random
from button import Button
# Import pygame.locals for easier access to key coordinates
from pygame.locals import *
from pygame import mixer
from setup import *
from particles import Particles
from player import *
from meteor import Meteor

# Initialize pygame
pygame.init()

clock = pygame.time.Clock()

mixer.init()
mixer.music.load('assets/sounds/music.wav')
mixer.music.play()
# Main loop
runing = True

buttons = []

player = Player()

METEOR_EVENT = pygame.USEREVENT + 2
RELOAD_EVENT = pygame.USEREVENT+3
pygame.time.set_timer(METEOR_EVENT,1000)
pygame.time.set_timer(RELOAD_EVENT, 1)
while runing:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == QUIT:
			runing = False
		if event.type == PARTICLE_EVENT:
			particles.add_particles(player.x, player.y)
		if event.type == METEOR_EVENT:
			meteors.append(Meteor())
		if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
			if len(bullets) < 5:
				bullets.append(Bullet(player.x, player.y))
	screen.blit(bg,(0,0))
	player.draw()
	player.update()
	#player.shoot()
	for i in meteors:
		i.draw()
		i.update()
		if i.y>900:
			meteors.pop(meteors.index(i))
	for i in bullets:
		i.draw()
		i.update()
	for i in meteors:
		for j in bullets:
			if j.hitbox.colliderect(i.hitbox):
				meteors.pop(meteors.index(i))
				bullets.pop(bullets.index(j))
	pygame.display.update()
pygame.quit()