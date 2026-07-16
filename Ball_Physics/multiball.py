import pygame

# Each ball task  will have its own surface

# First surface: Each bounce it changes color (vertical)
# Second surface: collides with other balls. bouncing along floor and walls
# Third surface: there will be platforms for balls to bounce off of
# fourth surface: raining balls (no platforms) bounce off floor
	# shrink in size each bounce
	# when ball is less than 1, remove ball

# BONUS surface: spinning surface and ball is going to roll based on direction of surface spinning


# INITALIZE
pygame.init()

# SURFACE CLASS
class Ball_Surface:
	def __init__(self, x_pos, y_pos, width, height, color):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.width = width
		self.height = height
		self.color = color

		self.surface = pygame.Surface((self.width, self.height))

	def draw_surface(self, surface):
		self.surface.fill(self.color)
		surface.blit(self.surface, (self.x_pos, self.y_pos))

# BALL CLASS
class Ball_Object:
	pass

# SCREEN
screen_w, screen_h = 800, 600

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Multi-Ball")

# OBJECTS
surface1 = Ball_Surface(10, 10, 100, 100, "pink")

# GAME LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("white")

	# DRAW
	surface1.draw_surface(screen)

	pygame.display.flip()

pygame.quit()
