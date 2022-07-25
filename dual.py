import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin PWM3.

pwm1 = pwmio.PWMOut(board.PWM1, frequency=50)
pwm2 = pwmio.PWMOut(board.PWM2, frequency=50)

# Create a servo object, my_servo.

my_servo_1 = servo.Servo(pwm1, actuation_range=360,
                                 min_pulse=500, max_pulse=2500)
my_servo_2 = servo.Servo(pwm2, actuation_range=270, min_pulse=500, max_pulse=2500)

while True:
    c = input("pan or tilt")
    if c == 'p':
        d = int(input("enter pan degree"))
        try:
           my_servo_1.angle = d
        except KeyboardInterrupt:
            continue
    elif c == 't':
        e = int(input("enter tilt degree"))
        try:
           my_servo_2.angle = e
        except KeyboardInterrupt:
            continue
    else:
        continue
