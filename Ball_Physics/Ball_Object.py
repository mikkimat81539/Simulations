import pygame

pygame.init()

class Ball:
	def __init__(self, x_pos, y_pos, radius, color, velocity):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.center = pygame.math.Vector2(self.x_pos, self.y_pos)

		self.radius = radius
		self.color = color

		self.activate = False

		self.velocity = velocity

	def draw_ball(self, surface):
		pygame.draw.circle(surface, self.color, self.center, self.radius)
