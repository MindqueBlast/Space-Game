import pygame, sys, random
from particles import Particles
from setup import *

global shootLoop
shootLoop = 0

particles = Particles()

PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT,50)

class Bullet():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.vel = 13
	def draw(self):
		screen.blit(bullet_img,(self.x, self.y))
	def update(self):
		if(self.y >-50):
			self.y-=self.vel
		else:
			for i in bullets:
				bullets.pop(bullets.index(i))
		self.hitbox = bullet_img.get_rect(topleft = (self.x, self.y))

class Player:
	def __init__(self):
		self.x = 700
		self.y = 400
		self.w = player_sprite.get_width()
		self.h = player_sprite.get_height()
		self.xvel = 0
		self.yvel = 0
		self.speed = 1
		self.angle = 0
		self.img = player_sprite
	def draw(self):		
		# offset from pivot to center
		image_rect = self.img.get_rect(topleft = (self.x - self.w/2, self.y-self.h/2))
		offset_center_to_pivot = pygame.math.Vector2((self.x, self.y)) - image_rect.center
	
		# roatated offset from pivot to center
		rotated_offset = offset_center_to_pivot.rotate(-self.angle)

		# roatetd image center
		rotated_image_center = (self.x - rotated_offset.x, self.y - rotated_offset.y)

		# get a rotated image
		rotated_image = pygame.transform.rotate(self.img, self.angle)
		rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
		self.hitbox = rotated_image_rect
		# rotate and blit the image
		screen.blit(rotated_image, rotated_image_rect)
	
		# draw rectangle around the image
		pygame.draw.rect(screen, (255, 0, 0), (*rotated_image_rect.topleft, *rotated_image.get_size()),2)
	def update(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			self.xvel += self.speed
			self.angle = -15
		elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
			self.xvel -= self.speed
			self.angle = 15
		else:
			self.angle = 0

		if keys[pygame.K_UP] or keys[pygame.K_w]:
			self.yvel -= self.speed
		elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
			self.yvel += self.speed

		self.xvel /= 1.15
		self.yvel /= 1.15

		self.x += self.xvel
		self.y += self.yvel


	def shoot(self):
		global shootLoop
		keys = pygame.key.get_pressed()
		if shootLoop > 0:
			shootLoop += 1
		if shootLoop > 3:
			shootLoop = 0
		if keys[pygame.K_SPACE] and shootLoop == 0:
			bullets.append(Bullet(self.x, self.y))
