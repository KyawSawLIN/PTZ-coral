import time
import board
import pwmio
import sys
from adafruit_motor import servo

# create a PWMOut object on Pin PWM3.

pwm1 = pwmio.PWMOut(board.PWM1, frequency=50)
pwm2 = pwmio.PWMOut(board.PWM2, frequency=50)

list_t = [90]   # to store previous tilt angles : initial angle is 90 degree
list_p = [0]    # to store previous pan angles : initial angle is 0 degree
counter = 1
pan_counter = 1

# Create a servo object, my_servo.

my_servo_1 = servo.Servo(pwm1, actuation_range=360,
                         min_pulse=500, max_pulse=2500)  # pan motion
my_servo_2 = servo.Servo(pwm2, actuation_range=270,
                         min_pulse=500, max_pulse=2500)  # tilt motion


def tilt_servo_control(current_pan_angle,counter):


   list_t.append(current_pan_angle)
   print("previous tilt angles : ", list_t)
   print(counter)
   previous_pan_angle = list_t[counter-1]
   
   while previous_pan_angle != current_pan_angle:

        if previous_pan_angle < current_pan_angle:
            for i in range(previous_pan_angle, current_pan_angle+5, 5):
                my_servo_2.angle = i
                time.sleep(0.1)
                print("angle ## ", i)
                previous_pan_angle = i

        if previous_pan_angle > current_pan_angle:
            for j in range(previous_pan_angle, current_pan_angle-5, -5):
                my_servo_2.angle = j
                time.sleep(0.1)
                print("angle ## ", j)
                previous_pan_angle = j


while 1:

    c = input("pan or tilt")
    my_servo_1.angle = list_p[pan_counter-1]

    if c == 'p':
        d = int(input("enter pan degree"))
        pan_counter += 1
        list_p.append(d)
        print("previous pan angles : ", list_p)
        try:
            my_servo_1.angle = d
        except KeyboardInterrupt:
            continue

    elif c == 't':
        current_angle = int(input("enter tilt degree"))
        if current_angle <= 180:
            tilt_servo_control(current_angle, counter)
            counter += 1

        else:
            print("tilt angle range is from 0 t 180")
            continue

    elif c == 'i':  # reset servos to initial positions and kill the program at the same time
        my_servo_1.angle = 0

        tilt_servo_control(90,counter)

        sys.exit(0)

    else:
        continue
