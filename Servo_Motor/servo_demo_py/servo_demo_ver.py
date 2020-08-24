import pigpio
from time import sleep

pi = pigpio.pi()

val1 = 1200
pulse = 0

# GPIO #17 => Vertical Servo.
while True:
    pi.set_servo_pulsewidth(17,   0) # PWM off
    sleep(1)
    for i in range(1000):
        pulse = 900 + i
        pi.set_servo_pulsewidth(17, pulse) # PWM off
        sleep(0.002)
        if(pulse == 1400):
            sleep(2)
    pi.set_servo_pulsewidth(17,   0) # PWM off
    sleep(1)
