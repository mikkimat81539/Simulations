import pygame

# Each ball will have its own surface

# First surface: Each bounce it changes color (vertical)
# Second surface: collides with other balls. bouncing along floor and walls
# Third surface: there will be platforms for balls to bounce off of
# fourth surface: raining balls (no platforms) bounce off floor
	# shrink in size each bounce
	# when ball is less than 1, remove ball
# fifth surface: have balls stick together and still bounce off of borders 

pygame.init()

screen = pygame.display.set_mode((800, 600))
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
