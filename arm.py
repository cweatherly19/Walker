#to access files needed to run the code
import curses
import setup
import RoboPiLib as RPL
#to define motor position
motor1 = 0
motor2 = 1
speed = 1
#to define the 'screen' in front of functions
screen = curses.initscr()
#to read key inputs
key = ''
#to set motor position
place = 400
place2 = 400
RPL.servoWrite(motor2, place)
RPL.servoWrite(motor1, place2)
screen.addstr('Hit Q to quit. Use the W, A, S, and D to test if code works. Hit E or R to      change speed. Detected key: ')
#to end loop if 'q' is hit
while key != ord('q'):
    #so the key can be read
    key = screen.getch()
    screen.clear()
    screen.addstr('Hit Q to quit. Use the W, A, S, and D to test if code works. Hit E or R to      change speed. Detected key: ')
    #to define what keys preform commands
    if key == ord('w'):
        screen.addstr('w key')
        place = place + (10 * speed)
        if place > 2400:
            place = 2400
        RPL.servoWrite(motor2, place)
    elif key == ord('s'):
        screen.addstr('s key')
        place = place - (10 * speed)
        if place < 400:
           place = 400
        RPL.servoWrite(motor2, place)
    elif key == ord('a'):
        screen.addstr('a key')
        place2 = place2 + (10 * speed)
        if place2 > 2400:
            place2 = 2400
        RPL.servoWrite(motor1, place2)
    elif key == ord('d'):
        screen.addstr('d key')
        place2 = place2 - (10 * speed)
        if place2 < 400:
            place2 = 400
    elif key == ord('e'):
        speed = 2 * speed
        if speed > 8:
            speed = 8
    elif key == ord('r'):
        speed = 0.5 * speed
        if speed < 1:
            speed = 1
        RPL.servoWrite(motor1, place2)
    else:
        screen.addstr('void')
    #to reformat the terminal/end the curses program
    screen.addstr(' place: ')
    screen.addstr(str(place))
    screen.addstr(' place2: ')
    screen.addstr(str(place2))
    screen.addstr(' speed: ')
    screen.addstr(str(speed))
    curses.endwin()
