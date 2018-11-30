# inverse kinimatics code
import math
import time
import RoboPiLib as RPL
s_pin = 0 # shoulder pin
e_pin = 1 # elbow pin
RPL.servoWrite(s_pin, 1400)
RPL.servoWrite(e_pin, 400)
d_one = 10 # the distance from shoulder to elbow
d_two = 10 # distance from elbow to wrist
fraction_shoulder = 1 / 1 # gear ration for shoulder motor
fraction_elbow = 1 / 1 # gear ratio for elbow motor
# to determine where the arm should go
while True:
    print 'Enter x value'
    x = input('- ') # given x input
    print 'Enter y value'
    y = input('- ') # given y input
############################################################################################################
    start = time.time() # to test how long it takes the code to run
    d_three = math.sqrt(math.pow(y, 2) + math.pow(x, 2)) # determine distance from shoulder to wrist
    # to see if reaching the point is possible
    outer_reach = d_one + d_two # determine if the point is too far
    if d_three > outer_reach:
        print 'Out of reach: too far away.'
        continue
    inner_reach = d_one - d_two # determine if the point is too close
    if d_three < inner_reach:
        print 'Out of reach: too close.'
        continue
    if y == x == 0:
        print 'Too close to origin.'
        continue
    # finding angle values
    a_three = math.acos((math.pow(d_one, 2) + math.pow(d_two, 2) - math.pow(y, 2) - math.pow(x, 2)) / (2 * d_one * d_two)) # angle for elbow
    a_two = math.asin(d_two * math.sin(a_three) / d_three) # angle between shoulder and wrist
    a_four = math.atan2(y,x) # angle between 0 line and wrist
    # check if values are possible or not
    print 'Situation in relations to axis: (%i, %i)' %(x, y)
    if y >= 0:
        print 'Point above x axis'
        a_shoulder = a_four + a_two
    elif a_two >= math.fabs(a_four):
        print 'Point above x axis, elbow is not'
        a_shoulder = a_two - a_four
    elif a_two < math.fabs(a_four):
        print 'Arm below x axis'
        a_shoulder = a_two - math.fabs(a_four)
    # to give outputs
    input_elbow = int(a_three * 2000 / math.pi + 400) # so the elbow will be at its floor at the minimum value
    input_shoulder = int(a_shoulder * 2000 / math.pi + 1400) # so there can be negative y values
    print_shoulder = a_shoulder * 180 / math.pi
    print_elbow = a_three * 180 / math.pi
    end = time.time()
    RPL.servoWrite(s_pin, input_shoulder)
    RPL.servoWrite(e_pin, input_elbow)
############################################################################################################
    print 'Distance from base: %i units' % d_three
    print 'Shoulder: %i degrees' % print_shoulder
    print 'Elbow: %i degrees' % print_elbow
    print 'Shoulder motor value: %i' % input_shoulder
    print 'Elbow motor value: %i' % input_elbow
    print 'Time to get answer:'
    print end - start
    continue
