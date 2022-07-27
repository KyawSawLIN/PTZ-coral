import time
import board
import pwmio
import sys
from adafruit_motor import servo

# create a PWMOut object on Pin PWM3.

pwm1 = pwmio.PWMOut(board.PWM1, frequency=50)
pwm2 = pwmio.PWMOut(board.PWM2, frequency=50)

list_t = [90]
list_p = [0]
counter = 1
pan_counter = 1

# Create a servo object, my_servo.

my_servo_1 = servo.Servo(pwm1, actuation_range=360,
                         min_pulse=500, max_pulse=2500)  # pan motion
my_servo_2 = servo.Servo(pwm2, actuation_range=270,
                         min_pulse=500, max_pulse=2500)  # tilt motion


while 1:

    c = input("pan or tilt")
    my_servo_1.angle = list_p[pan_counter-1]

    if c == 'p':
        d = int(input("enter pan degree"))
        pan_counter += 1
        list_p.append(d)
        try:
            my_servo_1.angle = d
        except KeyboardInterrupt:
            continue

    elif c == 't':
        current_pan_angle = int(input("enter tilt degree"))
        list_t.append(current_pan_angle)
        print("previous tilt angles : ", list_t)
        print(counter)
        previous_pan_angle = list_t[counter-1]

        while previous_pan_angle != current_pan_angle:

            if previous_pan_angle < current_pan_angle:
                for i in range(previous_pan_angle, current_pan_angle+5 , 5):
                    my_servo_2.angle = i
                    time.sleep(0.1)
                    print("angle ## ", i)
                    previous_pan_angle = i

            if previous_pan_angle > current_pan_angle:
                for j in range(previous_pan_angle, current_pan_angle-5 , -5):
                    my_servo_2.angle = j
                    time.sleep(0.1)
                    print("angle ## ", j)
                    previous_pan_angle = j
        counter += 1

    elif c == 'i':  # reset servos to initial positions and kill the program at the same time
        my_servo_1.angle = 0
        list_t.append(90)
        print('count = ', counter)
        e = list_t[counter-1]
        print("previous tilt angles : ", list_t)
        print('resetting to initial positions')

        while e != 90:

            if e < 90:
                for i in range(e, 95, 5):
                    my_servo_2.angle = i
                    time.sleep(0.1)
                    print('angle ## ', i)
                    e = i
            if e > 90:
                for j in range(e, 85, -5):
                    my_servo_2.angle = j
                    time.sleep(0.1)
                    print("angle ## ", j)
                    e = j
        counter += 1

        sys.exit(0)

    else:
        continue
