import pigpio
from time import sleep

pi = pigpio.pi()

val1 = 1200
pulse = 0

# GPIO #17 => Vertical Servo.
while True:
    pi.set_servo_pulsewidth(17,   0) # PWM off
    sleep(1)
    for i in range(500):
        pulse = 910 - i
        if(900 > pulse > 880):
            pulse = 900
            pi.set_servo_pulsewidth(17, 0) # PWM 3/4 on
            sleep(0.03)
        else:
            pi.set_servo_pulsewidth(17, pulse) # PWM 3/4 on
            sleep(1)
    pi.set_servo_pulsewidth(17,   0) # PWM off
    sleep(1)
