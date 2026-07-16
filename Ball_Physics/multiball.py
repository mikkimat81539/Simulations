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

		self.rect = self.surface.get_rect(topleft=(self.x_pos, self.y_pos))

	def draw_surface(self, surface):
		# rect = self.surface.get_rect(topleft=(self.x_pos, self.y_pos))

		surface.blit(self.surface, self.rect)
		self.surface.fill(self.color)

# BALL CLASS
class Ball_Object:
	def __init__(self, x_pos, y_pos, radius, color):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.center = pygame.math.Vector2(self.x_pos, self.y_pos)

		self.radius = radius
		
		self.color = color

	def draw_object(self, surface):
		pygame.draw.circle(surface, self.color, self.center, self.radius)

# SCREEN
screen_w, screen_h = 800, 600

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Multi-Ball")

# SURFACE OBJECTS
surface1 = Ball_Surface(10, 10, 200, 200, "pink")

# BALL OBJECTS
ball1 = Ball_Object(surface1.rect.centerx - 10, surface1.rect.centery - 10, 10, "white")

# GAME LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("white")

	# DRAW
	ball1.draw_object(surface1.surface)
	surface1.draw_surface(screen)

	pygame.display.flip()

pygame.quit()
