import math
import fractions
import setup
import RoboPiLib as RPL

s_pin = 1
e_pin = 0

d_one = 12 # this is the distance from shoulder to elbow
d_two = 14 # distance from elbow to wrist
sqd_one = math.pow(d_one, 2)
sqd_two = math.pow(d_two, 2)

RPL.servoWrite(s_pin, 400)
RPL.servoWrite(e_pin, 400)

#set up gear ratios
print 'Enter numerator value for shoulder gear-ratio (connected to motor):'
sm_teeth = input('- ')
print 'Enter demoninator value for shoulder gear-ratio (off motor):'
sj_teeth = input('- ')
fraction1 = fractions.Fraction(sj_teeth, sm_teeth)

print 'Enter numerator value for elbow gear-ratio (connected to motor):'
em_teeth = input('- ')
print 'Enter demoninator value for elbow gear-ratio (off motor):'
ej_teeth = input('- ')
fraction2 = fractions.Fraction(ej_teeth, em_teeth)

while True:
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

    ######################################################################

    a_elbow = (a_elbow * 2000 / math.pi) * fraction2 + 400
    a_shoulder = (a_shoulder * 2000 / math.pi) * fraction1 + 400

    print 'Motor positions:'
    print int(a_elbow)
    print int(a_shoulder)

    print '(x, y) coordinate: (%i, %i)' %(x, y)

    if a_elbow > 2000:
        a_elbow = 2000
        print 'Elbow gear ratio prohibiting motion.'
    if a_shoulder > 2000:
        a_shoulder = 2000
        print 'Shoulder gear ration prohibiting motion.'
    RPL.servoWrite(s_pin, int(a_elbow))
    RPL.servoWrite(e_pin, int(a_shoulder))
    print 'Enter a new input? (yes/no)'
    go_again = raw_input('- ')
    if go_again == 'yes':
        continue
    else:
        break
