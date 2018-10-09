import math
import setup
import RoboPiLib as RPL

while True:
    s_pin = 1
    e_pin = 0

    d_one = 12 # this is the distance from shoulder to elbow
    d_two = 14 # distance from elbow to wrist
    sqd_one = math.pow(d_one, 2)
    sqd_two = math.pow(d_two, 2)

    print 'Enter x value'
    x = input('- ') # given x input- how we tell robot where to go
    print 'Enter y value'
    y = input('- ') # given y input- how we tell robot where to go

    #####################################################################################################

    d_three = math.sqrt(math.pow(y, 2) + math.pow(x, 2)) # determining distance from shoulder to wrist
    sqd_three = math.pow(d_three, 2)
    a_three = math.acos((sqd_one + sqd_two - sqd_three) / (2 * d_one * d_two)) # angle of elbow using law of cosines
    a_two = math.asin((d_two * math.sin(a_three)) / d_three) # angle between shoulder and wrist (put in a try?)
    a_one = 2 * math.pi - (a_three + a_two) # angle between elbow and shoulder (dont really need)
    a_four = math.atan(y / x) # angle between 0 line and wrist

    a_shoulder = a_four + a_two # angle the shoulder joint should be at from the 0 line
    a_elbow = a_three # elbow angle, flush back to shoulder is 0

    ###

    a_elbow = (a_elbow * 2000 / math.pi) + 400
    a_shoulder = (a_shoulder * 2000 / math.pi) + 400

    print int(a_elbow)
    print int(a_shoulder)

    RPL.servoWrite(s_pin, a_elbow)
    RPL.servoWrite(e_pin, a_shoulder)
    continue
