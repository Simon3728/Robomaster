from enum import Enum
import time

# Define an enumeration for the positions
class Rotation(Enum):
    CLOCKWISE = 1
    ANTICLOCKWISE = 2

def rotate_on_spot(ep_chassis, speed, rotation):
    if rotation == Rotation.ANTICLOCKWISE:
        ep_chassis.drive_wheels(w1=speed, w2=-speed, w3=-speed, w4=speed)
    else:
        ep_chassis.drive_wheels(w1=-speed, w2=speed, w3=speed, w4=-speed)

def drive_forward(ep_chassis, speed):
    ep_chassis.drive_wheels(w1=speed, w2=speed, w3=speed, w4=speed)

def drive_forward_time(ep_chassis, speed, duration):
    ep_chassis.drive_wheels(w1=speed, w2=speed, w3=speed, w4=speed)
    time.sleep(duration)
    stop_moving(ep_chassis)

def drive_backward(ep_chassis, speed):
    ep_chassis.drive_wheels(w1=-speed, w2=-speed, w3=-speed, w4=-speed)

def drive_backward_time(ep_chassis, speed, duration):
    ep_chassis.drive_wheels(w1=-speed, w2=-speed, w3=-speed, w4=-speed)
    time.sleep(duration)
    stop_moving(ep_chassis)

def stop_moving(ep_chassis):
   ep_chassis.drive_wheels(w1=0, w2=0, w3=0, w4=0)
