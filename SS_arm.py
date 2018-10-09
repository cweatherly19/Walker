#to access files needed to run the code
import curses
import setup
import RoboPiLib as RPL
#to define the 'screen' in front of functions
screen = curses.initscr()
#to define motor position
motor1 = 0
motor2 = 1
#to read key inputs
key = ''
#to set motor position
place = 400
place2 = 400
#set multiplier of speed
speed = 1
#set positions of motors
RPL.servoWrite(motor2, int(place))
RPL.servoWrite(motor1, int(place2))
#to tell the user what to do
screen.addstr('Hit Q to quit. Use the W, A, S, and D to test if code works. Hit E or R to      change speed. place: 400 place2: 400 speed: 1')
#to end loop if 'q' is hit
while key != ord('q'):
    #so the key can be read
    key = screen.getch()
    screen.clear()
    screen.addstr('Hit Q to quit. Use the W, A, S, and D to test if code works. Hit E or R to      change speed.')
    screen.addstr(' place: ')
    screen.addstr(str(place))
    screen.addstr(' place2: ')
    screen.addstr(str(place2))
    screen.addstr(' speed: ')
    screen.addstr(str(speed))
    if key == ord('r'):
        speed = speed * 2
        if speed > 8:
            speed = 8
    elif key == ord('e'):
        speed = speed / 2
        if speed < 1:
            speed = 1
    #to define what keys preform commands
    elif key == ord('w'):
        place = place + int(10 * speed)
        if place > 2400:
            place = 2400
        RPL.servoWrite(motor2, int(place))
    elif key == ord('s'):
        place = place - int(10 * speed)
        if place < 400:
           place = 400
        RPL.servoWrite(motor2, int(place))
    elif key == ord('a'):
        place2 = place2 + int(10 * speed)
        if place2 > 2400:
            place2 = 2400
        RPL.servoWrite(motor1, int(place2))
    elif key == ord('d'):
        place2 = place2 - int(10 * speed)
        if place2 < 400:
            place2 = 400
        RPL.servoWrite(motor1, int(place2))
    else:
        screen.addstr(' invalid input')
    #to reformat the terminal/end the curses program
    curses.endwin()
