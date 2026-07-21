# Create ball
# Create and display a charge
	# To display charge have a block increase in height as spacebar is held
	# When spacebar is held velocity will increase (max 20)
	# When spacebar is release the ball should move based on charged velocity 

import curses

# initalize screen
screen = curses.initscr()

class Ball:
	def __init__(self, y_pos, x_pos, text):
		self.y_pos = y_pos
		self.x_pos = x_pos
		self.text = text

		self.velocity = 1

		# save current position for next frame
		self.prev_x = self.x_pos
		self.prev_y = self.y_pos

	def draw_ball(self, surface):
		# Erase previous position
		surface.addstr(int(self.prev_y / 2), int(self.prev_x // 2), "")

		# new position
		surface.addstr(int(self.y_pos / 2), int(self.x_pos // 2), self.text)

		curses.napms(16) # pauses the program for a number of milliseconds.

		self.prev_x = self.x_pos
		self.prev_y = self.y_pos


	def move_ball(self, surface, surface_height):
		while True:
			dt = 1 / 60 # FPS

			self.y_pos += self.velocity * dt

			print(self.y_pos)

			self.draw_ball(surface)
			
			surface.refresh()

def main(surface):
	surface.clear()
	curses.noecho() # Do not show keys pressed

	win_x = 30 # window x_pos of where it should be on init screen
	win_y = 0 # window y_pos of where it should be on the init screen
	win_height = 20 # window height
	win_width = 50 # window width

	win = curses.newwin(win_height, win_width, win_y, win_x) # create window on top of inital window

	win.border() # show window outline

	curses.curs_set(0) # cursor visibility

	ball = Ball(win_height, win_width, "O") # ball object

	ball.move_ball(win, win_height) # moving the ball
	# ball.draw_ball(win) # Display ball

	with open("speed.txt", "x") as f:
		f.write(f"{ball.y_pos}")


	win.refresh()

	win.getkey()

	curses.endwin()	

main(screen)
