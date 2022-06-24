import pygame, sys, random
from setup import *

class Particles:
	def __init__(self):
		self.particles = []
	def emit(self):
		colors = ["Red", "Orange", "Yellow"]
		if self.particles:
			self.delete_particles()
			for particle in self.particles:
				particle[0][1] += particle[2][0]
				particle[0][0] += particle[2][1]
				particle[1] -= 0.2
				pygame.draw.circle(screen,pygame.Color(random.choice(colors)),particle[0], int(particle[1]))

	def add_particles(self, x, y):
		pos_x = x
		pos_y = y+30
		radius = 10
		direction_y = random.randint(-3,3)
		direction_x = random.randint(1,3)
		particle_circle = [[pos_x,pos_y],radius,[direction_x,direction_y]]
		self.particles.append(particle_circle)

	def delete_particles(self):
		particle_copy = [particle for particle in self.particles if particle[1] > 0]
		self.particles = particle_copy