import pygame

# Each ball task  will have its own surface

# First surface: Each bounce it changes color (vertical)
# Second surface: collides with other balls. bouncing along floor and walls
# Third surface: there will be platforms for balls to bounce off of
# fourth surface: raining balls (no platforms) bounce off floor
	# shrink in size each bounce
	# when ball is less than 1, remove ball

# fifth surface: have a ball bounce off of roof, wall and moving platform controlle with keys
	# similar to brick breaker

# sixth surface: spinning surface and ball is going to roll based on direction of surface spinning


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

# PLATFORM CLASS
class Platforms:
	def __init__(self, x_pos, y_pos, color):
		self.x_pos = x_pos
		self.y_pos = y_pos
		
		self.start_pos = pygame.math.Vector2(self.x_pos, self.y_pos)
		self.end_pos = pygame.math.Vector2(self.start_pos[0] + 10, self.start_pos[1])

		self.color = color

	def draw_platform(self, surface):
		pygame.draw.line(surface, self.color, self.start_pos, self.end_pos, 3)


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
