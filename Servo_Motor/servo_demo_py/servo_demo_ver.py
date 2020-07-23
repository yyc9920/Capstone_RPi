import pigpio
from time import sleep

pi = pigpio.pi()

# GPIO #17 => Vertical Servo.
while True:
    pi.set_PWM_dutycycle(17,   0) # PWM off
    sleep(1)
    pi.set_PWM_dutycycle(17, 25) # PWM 1/4 on
    sleep(1)
    pi.set_PWM_dutycycle(17, 50) # PWM 1/2 on
    sleep(1)
    pi.set_PWM_dutycycle(17, 10) # PWM 3/4 on
    sleep(1)
