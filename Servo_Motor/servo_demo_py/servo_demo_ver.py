import pigpio
from time import sleep

pi = pigpio.pi()

# GPIO #17 => Vertical Servo.
while True:
    pi.set_servo_pulsewidth(17,   0) # PWM off
    sleep(1)
    pi.set_servo_pulsewidth(17, 2000) # PWM 1/4 on
    sleep(1)
    pi.set_servo_pulsewidth(17,   0) # PWM off
    sleep(1)
    pi.set_servo_pulsewidth(17, 2300) # PWM 1/2 on
    sleep(1)
    pi.set_servo_pulsewidth(17,   0) # PWM off
    sleep(1)
    pi.set_servo_pulsewidth(17, 1700) # PWM 3/4 on
    sleep(1)
    pi.set_servo_pulsewidth(17,   0) # PWM off
    sleep(1)
