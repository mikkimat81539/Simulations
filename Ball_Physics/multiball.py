import pygame, random, math

# Each ball task  will have its own surface

# First surface: Each bounce it changes color (vertical) -- DONE
# Second surface: collides with other balls. bouncing along floor and walls -- DONE

# Third surface: get two balls to collide with each other -- DONE

# Fourth surface: have a ball bounce off of roof, wall and moving platform controlled with keys
	# similar to brick breaker


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

	def move_object(self, surface): # for movement along x and y axis with collision
		self.center[0] += self.velocity_x
		self.center[1] += self.velocity_y

		if self.center[0] - self.radius <= 5 or self.center[0] + self.radius >= surface.width:
			self.velocity_x = -self.velocity_x

		if self.center[1] - self.radius <= 5 or self.center[1] + self.radius >= surface.width:
			self.velocity_y = -self.velocity_y

class Platform:
	def __init__(self, x_pos, y_pos, thickness, color):
		self.x_pos = x_pos
		self.y_pos = y_pos
		
		self.start_pos = pygame.math.Vector2(self.x_pos, self.y_pos)
		self.end_pos = pygame.math.Vector2(self.start_pos[0] + 160, self.start_pos[1])

		self.thickness = thickness
		self.color = color

		self.vel_x = 5
		self.vel_y = 5

	def draw_platform(self, surface):
		pygame.draw.line(surface, self.color, self.start_pos, self.end_pos, self.thickness)

	def move_platform(self):
		key = pygame.key.get_pressed()

		if key[pygame.K_LEFT]:
			self.start_pos[0] -= self.vel_x
			self.end_pos[0] -= self.vel_x

		if key[pygame.K_RIGHT]:
			self.start_pos[0] += self.vel_x
			self.end_pos[0] += self.vel_x

		if key[pygame.K_UP]:
			self.start_pos[1] -= self.vel_y
			self.end_pos[1] -= self.vel_y

		if key[pygame.K_DOWN]:
			self.start_pos[1] += self.vel_y
			self.end_pos[1] += self.vel_y


		self.collision()

	def collision(self):
		if self.start_pos[0] < 5: # LEFT SIDE
			self.start_pos[0] += self.vel_x
			self.end_pos[0] += self.vel_x

		if self.end_pos[0] > 195: # RIGHT SIDE
			self.start_pos[0] -= self.vel_x
			self.end_pos[0] -= self.vel_x

		if self.start_pos[1] < 130: # TOP SIDE
			self.start_pos[1] += self.vel_y
			self.end_pos[1] += self.vel_y

		if self.end_pos[1] > self.y_pos: # BOTTOM SIDE
			self.start_pos[1] -= self.vel_y
			self.end_pos[1] -= self.vel_y


class Blocks:
	def __init__(self, x_pos, y_pos, width, height, color):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.width = width
		self.height = height
		self.color = color

		self.rect = pygame.Rect((self.x_pos, self.y_pos), (self.width, self.height))

	def draw_blocks(self, surface):
		pygame.draw.rect(surface, self.color, self.rect)

# CLOCK
clock = pygame.time.Clock()

# SCREEN
screen_w, screen_h = 850, 300

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Multi-Ball")

# SURFACE OBJECTS
surface1 = Ball_Surface(10, 10, 200, 200, "pink")
surface2 = Ball_Surface(220, 10, 200, 200, "#82edf5")
surface3 = Ball_Surface(430, 10, 200, 200, "#7ff58f")
surface4 = Ball_Surface(640, 10, 200, 200, "#ffed75")

# BALL OBJECTS
ball1 = Ball_Object(surface1.rect.centerx - 10, 20, 10, "white")

ball_list = [Ball_Object(random.randint(10, 70), random.randint(10, 70), 10, "black"), Ball_Object(random.randint(10, 70), random.randint(10, 70), 10, "white"), Ball_Object(random.randint(10, 70), random.randint(10, 70), 10, "purple")]


ball2 = Ball_Object(25, 100, 20, "yellow") 
ball2.velocity_x = 5
ball2.velocity_y = 0

ball3 = Ball_Object(175, 100, 20, "orange") 
ball3.velocity_x = 5
ball3.velocity_y = 0

ball4 = Ball_Object(100, 170, 10, "green")
ball4.velocity_x = 0
ball4.velocity_y = -7


# PLATFORM OBJECT
ground1 = Platform(20, 150, 4, "black")

platform = Platform(70, 180, 10, "blue")
platform.end_pos[0] = 130

# BLOCK
block1 = Blocks(50, 20, 50, 20, "gray")

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


def ball_collision(ball_1, ball_2, ball1_speed, ball2_speed): # Collision between two points

	x_eval = (ball_2.center[0] - ball_1.center[0]) ** 2 # (x2 - x1)^2
	y_eval = (ball_2.center[1] - ball_1.center[1]) ** 2 # (y2 - y1)^2


	distance_formula = int(math.sqrt(x_eval + y_eval))

	radii = ball_1.radius + ball_2.radius

#	print(f"distance: {distance_formula}")
#	print(f"radii: {radii}")

	if distance_formula <= radii:
		ball1_speed = -ball1_speed
		ball2_speed = -ball2_speed


	return ball1_speed, ball2_speed

def platform_collision(ball, platform, ball_speed_x, ball_speed_y, surface):
	ball.center[0] += ball_speed_x
	ball.center[1] += ball_speed_y


	if platform.start_pos[0] <= ball.center[0] <= platform.end_pos[0] and ball.center[1] + ball.radius == platform.start_pos[1]: # Platform and Ball collision
		ball_speed_x = -ball_speed_x
		ball_speed_y = -ball_speed_y

	if ball.center[1] - ball.radius < 5: 
		ball_speed_y = -ball_speed_y

	return ball_speed_x, ball_speed_y



# GAME LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("white")

	# draw and movement for ball list
	for i in ball_list:
		i.move_object(surface2.surface)
		i.draw_object(surface2.surface)

	# MOVEMENT
	velocity1 = movement1(ball1, ground1, velocity1, gravity1)

	ball2.move_object(surface3.surface)
	ball3.move_object(surface3.surface)

	# platform movement
	platform.move_platform()

	# COLLISION
	ball2.velocity_x, ball3.velocity_x = ball_collision(ball2, ball3, ball2.velocity_x, ball3.velocity_x)


	ball4.velocity_x, ball4.velocity_y = platform_collision(ball4, platform, ball4.velocity_x, ball4.velocity_y, surface4.surface)

	# DRAW
	
	# Balls
	ball1.draw_object(surface1.surface)

	ball2.draw_object(surface3.surface)
	ball3.draw_object(surface3.surface)

	ball4.draw_object(surface4.surface)


	# Platforms
	ground1.draw_platform(surface1.surface)
	platform.draw_platform(surface4.surface)

	# Blocks
	block1.draw_blocks(surface4.surface)

	# Surfaces
	surface1.draw_surface(screen)
	surface2.draw_surface(screen)
	surface3.draw_surface(screen)
	surface4.draw_surface(screen)

	pygame.display.flip()

	clock.tick(60)

pygame.quit()
