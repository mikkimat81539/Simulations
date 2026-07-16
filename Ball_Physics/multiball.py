import pygame

# Each ball task  will have its own surface

# First surface: Each bounce it changes color (vertical)
# Second surface: collides with other balls. bouncing along floor and walls
# Third surface: there will be platforms for balls to bounce off of
# fourth surface: raining balls (no platforms) bounce off floor
	# shrink in size each bounce
	# when ball is less than 1, remove ball

# BONUS surface: spinning surface and ball is going to roll based on direction of surface spinning
	# Use Math

pygame.init()

screen_w, screen_h = 800, 600

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Multi-Ball")

# Game Loop
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("white")

	pygame.display.flip()

pygame.quit()
