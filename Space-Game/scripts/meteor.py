import pygame, random, sys
from setup import *

class Meteor:
	def __init__(self):
		self.x = random.randint(100, 700)
		self.y =- 100
		self.vel = random.randint(3, 6)
		self.angle_vel = random.randint(-2, 2)
		self.img = random.choice(meteor_images)
		self.w = self.img.get_width()
		self.h = self.img.get_height()
		self.angle = 0
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
		self.y+=self.vel
		self.angle+=self.angle_vel-0.5
	