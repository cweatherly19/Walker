import math
import fractions
import setup
import RoboPiLib as RPL

s_pin = 1
e_pin = 0

#reset motor positions
RPL.servoWrite(s_pin, 400)
RPL.servoWrite(e_pin, 400)

print 'Enter distance from shoulder to elbow:'
d_one = input('- ') # this is the distance from shoulder to elbow

print ''

print 'Enter distance from elbow to wrist:'
d_two = input('- ') # distance from elbow to wrist
sqd_one = math.pow(d_one, 2)
sqd_two = math.pow(d_two, 2)

#set up gear ratios
print 'Enter numerator value for shoulder gear-ratio (connected to motor):'
sm_teeth = input('- ')
print 'Enter demoninator value for shoulder gear-ratio (off motor):'
sj_teeth = input('- ')
fraction_shoulder = fractions.Fraction(sj_teeth, sm_teeth)

print 'Enter numerator value for elbow gear-ratio:'
em_teeth = input('- ')
print 'Enter demoninator value for elbow gear-ratio:'
ej_teeth = input('- ')
fraction_eblow = fractions.Fraction(ej_teeth, em_teeth)

# NEED GEAR RATIOS FOR THIS TO WORK #

while True:
    print 'Enter x value'
    x = input('- ') # given x input- how we tell robot where to go

    print ''

    print 'Enter y value'
    y = input('- ') # given y input- how we tell robot where to go

    print ''

    #####################################################################################################

    d_three = math.sqrt(math.pow(y, 2) + math.pow(x, 2)) # determining distance from shoulder to wrist
    sqd_three = math.pow(d_three, 2)
    a_three = math.acos((sqd_one + sqd_two - sqd_three) / (2 * d_one * d_two)) # angle of elbow using law of cosines
    a_two = math.asin((d_two * math.sin(a_three)) / d_three) # angle between shoulder and wrist (put in a try?)
    a_one = 2 * math.pi - (a_three + a_two) # angle between elbow and shoulder (dont really need)
    a_four = math.atan2(y , x) # angle between 0 line and wrist

    a_shoulder = a_four + a_two # angle the shoulder joint should be at from the 0 line
    a_elbow = a_three # elbow angle, flush back to shoulder is 0

    ######################################################################

    a_elbow = (a_elbow * 2000 / math.pi) * fraction_eblow + 400
    if a_elbow > 2400:
        print 'Elbow error'
        print ''
        a_elbow = 2400
    if a_elbow < 400:
        print 'Elbow error'
        print ''
        a_elbow = 400
    a_shoulder = (a_shoulder * 2000 / math.pi) * fraction_shoulder + 400
    if a_shoulder > 2400:
        print 'Shoulder error'
        print ''
        a_shoulder = 2400
    if a_shoulder < 400:
        print 'Shoulder error'
        print ''
        a_shoulder = 400
    print 'Motor positions:'
    print 'Elbow - %i' %a_elbow
    print 'Shoulder - %i' %a_shoulder
    print ''
    print '(x, y) coordinate: (%i, %i)' %(x, y)
    print ''
    print 'Enter a new input? (yes/no)'

    #move the motors to desired positions
    RPL.servoWrite(s_pin, int(a_elbow))
    RPL.servoWrite(e_pin, int(a_shoulder))

    go_again = raw_input('- ')
    if go_again == 'yes':
        print ''
        continue
    else:
        break
