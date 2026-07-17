import pygame, random

# Each ball task  will have its own surface

# First surface: Each bounce it changes color (vertical) -- DONE
# Second surface: collides with other balls. bouncing along floor and walls
	# When collision create additional balls
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

		self.velocity_x = random.randint(1, 20)
		self.velocity_y = random.randint(1, 20)

	def draw_object(self, surface):
		pygame.draw.circle(surface, self.color, self.center, self.radius)

	def move_object(self, surface):
		self.center[0] += self.velocity_x
		self.center[1] += self.velocity_y

		if self.center[0] - self.radius <= 5 or self.center[0] + self.radius >= surface.width:
			self.velocity_x = -self.velocity_x

		if self.center[1] - self.radius <= 5 or self.center[1] + self.radius >= surface.width:
			self.velocity_y = -self.velocity_y

class Platform:
	def __init__(self, x_pos, y_pos, color):
		self.x_pos = x_pos
		self.y_pos = y_pos
		
		self.start_pos = pygame.math.Vector2(self.x_pos, self.y_pos)
		self.end_pos = pygame.math.Vector2(self.start_pos[0] + 160, self.start_pos[1])

		self.color = color

	def draw_platform(self, surface):
		pygame.draw.line(surface, self.color, self.start_pos, self.end_pos, 4)

# CLOCK
clock = pygame.time.Clock()

# SCREEN
screen_w, screen_h = 800, 600

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Multi-Ball")

# SURFACE OBJECTS
surface1 = Ball_Surface(10, 10, 200, 200, "pink")
surface2 = Ball_Surface(220, 10, 200, 200, "#82edf5")

# BALL OBJECTS
ball1 = Ball_Object(surface1.rect.centerx - 10, 20, 10, "white")

ball_list = [Ball_Object(random.randint(10, 70), random.randint(10, 70), 10, "black"), Ball_Object(random.randint(10, 70), random.randint(10, 70), 10, "white"), Ball_Object(random.randint(10, 70), random.randint(10, 70), 10, "purple")]


# PLATFORM OBJECT
ground1 = Platform(20, 150, "black")

# SPEED
velocity1 = 5

# GRAVITY
gravity1 = 0.8 

# COLORS
ball_colors = ["red", "blue", "green", "yellow", "purple","orange", "cyan", "magenta", "lime","teal", "navy", "brown", "gray", "gold"]


# MOVEMENT FUNCTION
def movement1(ball, platform, velocity, gravity):
#	velocity += gravity
#	ball.center[1] += velocity

	# if ball.center[1] >= (platform.y_pos - (ball.radius - 5)): # move ball until it reaches ground
		# velocity = -velocity * gravity

	ball.center[1] = int(ball.center[1])

	if ball.center[1] < (platform.y_pos - (ball.radius - 5)):
		# print(f"START: {platform.y_pos - (ball.radius-10)}")
		# print(f"START ball {ball.center[1]}")
		velocity += gravity
		ball.center[1] += velocity

	elif ball.center[1] >= (platform.y_pos - (ball.radius - 5)):
#		print(f"Platform END: {platform.y_pos - (ball.radius-5)}")
#		print(f"ball {ball.center[1]}")
#
#		print(f"Velocity: {velocity}\n")

		ball.center[1] = platform.y_pos - ball.radius # reset the ball position after collision
		velocity = -velocity * gravity

		ball.color = random.choice(ball_colors)

		# if abs(velocity) < 7:
			# velocity = 0

	return velocity


# GAME LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("white")


	for i in ball_list:
		i.move_object(surface2.surface)
		i.draw_object(surface2.surface)

	# MOVEMENT
	velocity1 = movement1(ball1, ground1, velocity1, gravity1)

	# DRAW
	ball1.draw_object(surface1.surface)

	ground1.draw_platform(surface1.surface)

	surface1.draw_surface(screen)
	surface2.draw_surface(screen)

	pygame.display.flip()

	clock.tick(60)

pygame.quit()
