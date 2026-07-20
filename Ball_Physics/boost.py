# Create ball
# Create and display a charge
	# To display charge have a block increase in height as spacebar is held
	# When spacebar is held velocity will increase (max 20)
	# When spacebar is release the ball should move based on charged velocity 

import curses

# initalize screen
screen = curses.initscr()

def main(surface):
	surface.clear()
	curses.noecho()

	surface.addstr("O\n")

	surface.refresh()
	surface.getkey()

	curses.endwin()	

main(screen)
