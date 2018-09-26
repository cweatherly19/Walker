#to access files needed to run the code
import curses
import setup
import RoboPiLib as RPL
#to define motor position
motor1 = 0
motor2 = 1
#to define the 'screen' in front of functions
screen = curses.initscr()
#to read key inputs
key = ''
#to set motor position
place = 1000
place2 = 1000
RPL.servoWrite(motor2, place)
RPL.servoWrite(motor1, place2)
#to end loop if 'q' is hit
while key != ord('q'):
    #so the key can be read
    key = screen.getch()
    screen.clear()
    screen.addstr('Hit Q to quit. Use the W, A, S, and D to test if code works. Detected key: ')
    #to define what keys preform commands
    if key == ord('w'):
        screen.addstr('w key')
        place = place + 10
        if place > 2440:
            place = 2440
        RPL.servoWrite(motor2, place)
    elif key == ord('s'):
        screen.addstr('s key')
        place = place - 10
         if place < 390:
            place = 390
        RPL.servoWrite(motor2, place)
    elif key == ord('a'):
        screen.addstr('a key')
        place2 = place2 + 10
        if place2 > 2440:
            place2 = 2440
        RPL.servoWrite(motor1, place2)
    elif key == ord('d'):
        screen.addstr('d key')
        place2 = place2 - 10
        if place2 < 390:
            place2 = 390
        RPL.servoWrite(motor1, place2)
    #to reformat the terminal/end the curses program
    screen.addstr(' place: ')
    screen.addstr(str(place))
    screen.addstr(' place2: ')
    screen.addstr(str(place2))
    curses.endwin()
