import pigpio
from time import sleep

pi = pigpio.pi()

# GPIO #25 => Vertical Servo.
while True:
    #pi.set_servo_pulsewidth(25, 0)
    #sleep(1)
    #pi.set_servo_pulsewidth(25, 1600) # slowly turn right
    #sleep(1)
    #pi.set_servo_pulsewidth(25, 1350) # slowly turn left
    #sleep(1)
    pi.set_servo_pulsewidth(25, 1475) # halt
    sleep(1)
