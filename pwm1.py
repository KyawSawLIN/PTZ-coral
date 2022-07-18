import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin PWM3.
pwm = pwmio.PWMOut(board.PWM2, frequency=50)
pwm1 = pwmio.PWMOut(board.PWM1, frequency=50)

# Create a servo object, my_servo.
my_servo_1 = servo.Servo(pwm, actuation_range=270,
                         min_pulse=500, max_pulse=2500)
my_servo_2 = servo.Servo(pwm1, actuation_range=360,
                         min_pulse=200, max_pulse=3000)

while True:
    d = input("pan for 'p' and tilt for 't' : ")
    if d == 'p':
        try:
         while True: 
            # 0 - 180 degrees, 5 degrees at a time.
            for angle in range(0, 270, 5):
                my_servo_1.angle = angle
                time.sleep(0.05)
            # 180 - 0 degrees, 5 degrees at a time.
            for angle in range(270, 0, -5):
                my_servo_1.angle = angle
                time.sleep(0.05)
        except KeyboardInterrupt:
            continue
    elif d == 't':
        try:
          while True: 
            # 0 - 180 degrees, 5 degrees at a time.
            for angle in range(0, 360, 5):
                my_servo_2.angle = angle
                time.sleep(0.05)
            # 180 - 0 degrees, 5 degrees at a time.
            for angle in range(360, 0, -5):
                my_servo_2.angle = angle
                time.sleep(0.05)
        except KeyboardInterrupt:
            continue
    else : 
        continue 
