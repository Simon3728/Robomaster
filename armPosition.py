from enum import Enum

# Define an enumeration for the positions
class ArmPosition(Enum):
    BASE = 1
    PICKUP_1 = 2
    PICKUP_2 = 3
    COLLECT = 4
    FOLLOW = 5

def set_arm_position(ep_arm, position):
    # Move the arm to the specified position based on the parameter
    # Example to use the function: set_arm_position(ep_arm, ArmPosition.BASE)
    if position == ArmPosition.BASE:
        ep_arm.moveto(x=190, y=100).wait_for_completed()
    elif position == ArmPosition.PICKUP_1:
        ep_arm.moveto(x=190, y=100).wait_for_completed()
        ep_arm.moveto(x=96, y=80).wait_for_completed()
    elif position == ArmPosition.PICKUP_2:
        ep_arm.moveto(x=190, y=100).wait_for_completed()
        ep_arm.moveto(x=152, y=80).wait_for_completed()
    elif position == ArmPosition.COLLECT:
        ep_arm.moveto(x=190, y=100).wait_for_completed()
        ep_arm.moveto(x=190, y=-59).wait_for_completed()
    elif position == ArmPosition.FOLLOW:
        ep_arm.moveto(x=190, y=100).wait_for_completed()
        ep_arm.moveto(x=91, y=132).wait_for_completed()