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
	curses.noecho() # Do not show keys pressed

	win_x = 30 # window x_pos of where it should be on init screen
	win_y = 0 # window y_pos of where it should be on the init screen
	win_height = 20 # window height
	win_width = 50 # window width

	win = curses.newwin(win_height, win_width, win_y, win_x) # create window on top of inital window

	win.border() # show window outline

	curses.curs_set(0) # cursor visibility

	win.addstr(win_x // 2, win_y // 2, "O") # Display text on (y, x)

	win.refresh()
	win.getkey()

	curses.endwin()	

main(screen)
