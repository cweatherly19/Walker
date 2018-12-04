#the file that reads key inputs
import curses
#to set starting coordinates for curses to track
x = 10; y = 10
#for defining the lengths of the arm
segment_1 = 10; segment_2 = 10
#to enter into the curses screen
screen = curses.initscr()
#so important text can stand out
curses.start_color(); curses.use_default_colors(); curses.init_pair(1, curses.COLOR_RED, -1); curses.init_pair(2, curses.COLOR_GREEN, -1)
#so the only things that print are the returned values
curses.noecho()
#so the screen will update every tenth of a second (from 1 to 225)
curses.halfdelay(1)
#to set key value to be read later
key = ''
#to end loop if 'q' is hit
while key != ord('q'):
    #so key presses can be read
    key = screen.getch()
    #to reformat the screen every time something is hit
    screen.clear()
    #to format and give instructions for the arm use
    screen.addstr(0, 0, 'Hit   to quit. Use  ,  ,  , and   to move the arm.'); screen.addstr(0, 4, 'Q', curses.color_pair(1)); screen.addstr(0, 19, 'W', curses.color_pair(2)); screen.addstr(0, 22, 'A', curses.color_pair(2)); screen.addstr(0, 25, 'S', curses.color_pair(2)); screen.addstr(0, 32, 'D', curses.color_pair(2)); screen.addstr(0, 51, 'Detected key:')
    #to define what keys preform commands
    if key != curses.ERR: # This is true if the user pressed something
        if key == ord('w'):
            screen.addstr(0, 65, 'w key', curses.color_pair(2))
            #y = y + 0.2
        elif key == ord('s'):
            screen.addstr(0, 65, 's key', curses.color_pair(2))
            #y = y - 0.2
        elif key == ord('a'):
            screen.addstr(0, 65, 'a key', curses.color_pair(2))
            #x = x + 0.2
        elif key == ord('d'):
            screen.addstr(0, 65, 'd key', curses.color_pair(2))
            #x = x - 0.2
        else:
            screen.addstr(0, 65, 'invalid', curses.color_pair(1))
            #to signify that there is an invalid input
            curses.beep()
        #to reformat the terminal after the curses file closes
        curses.endwin()

