#to access files needed to run the code
import curses
import setup
import RoboPiLib as RPL
#to define motor position
motor1 = 0
motor2 = 1
#to define the 'screen' in front of functions
screen = curses.initscr()
curses.halfdelay(3) # How many tenths of a second are waited, from 1 to 255
#to read key inputs
key = ''
#to end loop if 'q' is hit
while key != ord('q'):
    #so the key can be read
    key = screen.getch()
    screen.clear()
    screen.addstr('Hit Q to quit. Use the W, A, S, and D to test if code works. Detected key: ')
    #to define what keys preform commands
    if key != curses.ERR: # This is true if the user pressed something
        if key == ord('w'):
            screen.addstr('w key')
            place = place + 10
            if place > 2000:
                place = 2000
            if place < 1000:
                place = 1000
            RPL.servoWrite(motor2, place)
        elif key == ord('s'):
            screen.addstr('s key')
            place2 = place - 10
            if place > 2000:
                place = 2000
            if place < 1000:
                place = 1000
            RPL.servoWrite(motor2, place)
        elif key == ord('a'):
            screen.addstr('a key')
            RPL.servoWrite(motor1, 1000)
        elif key == ord('d'):
            screen.addstr('d key')
            RPL.servoWrite(motor1, 2000)
    else:
        RPL.servoWrite(motor1, 0)
        RPL.servoWrite(motor2, 0)
    #to reformat the terminal/end the curses program
    curses.endwin()
