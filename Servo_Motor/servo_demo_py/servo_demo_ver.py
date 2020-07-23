import pigpio
from time import sleep

pi = pigpio.pi()

# GPIO #17 => Vertical Servo.
while True:
    pi.set_servo_pulsewidth(17, 0)
    sleep(1)
    pi.set_servo_pulsewidth(17, 2000) # Perpendicular Pulse Width
    sleep(1)
    pi.set_servo_pulsewidth(17, 2500) # 45
    sleep(1)
    pi.set_servo_pulsewidth(17, 1500) # 135
    sleep(1)
