from robomaster import robot, camera
import time
from armPosition import ArmPosition, set_arm_position
from getBit import collect_bit, find_bit, Color, check_color
from follow import find_person, follow, follow2
from driving import *
from enum import Enum
import cv2
import numpy as np


# Gibt den Zustand, in dem siche der Robomaster befindet
class Zustand(Enum):
    SUCHEN = 1
    VERFOLGEN = 2
    ABLEGEN = 3
    AUFNEHEMEN = 4
    WAIT = 5

def main():
    # Initialize
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")
    ep_arm = ep_robot.robotic_arm
    ep_camera = ep_robot.camera
    ep_chassis = ep_robot.chassis

    #Bits, die gerade gesucht werden
    pink = False
    violet = False
    light_blue = False
    blue = False
    green = True
    white = False
    black = False
    yellow = False

    # Zum testen des 
    # Bit suchens
    zustand = Zustand.VERFOLGEN
    set_arm_position(ep_arm, ArmPosition.FOLLOW)   

    ep_camera.start_video_stream(display=False, resolution=camera.STREAM_720P)
    
    #While schleife für generellen Betrieb
    while True:
        if zustand == Zustand.SUCHEN:
            result = check_color(pink, violet, light_blue, blue, green, white, black, yellow)
            if len(result) >= 1:
                color = result[0]
            else:
                zustand = Zustand.WAIT
                continue
            rotate_on_spot(ep_chassis, 20, Rotation.CLOCKWISE)
            while True:
                frame = ep_camera.read_cv2_image()
                bit = find_bit(frame, color)         
                if bit is not None:
                    x, y, w, h = bit
                    print(bit)
                    if collect_bit(ep_chassis, frame, x, y, w, h):
                        stop_moving(ep_chassis)
                        drive_forward_time(ep_chassis, 15, 2)
                        drive_backward_time(ep_chassis, 15, 3)    
                        start_time = time.time()
                        while True:
                            frame = ep_camera.read_cv2_image()
                            bit = find_bit(frame, color)
                            cv2.imshow("Camera", frame)
                            cv2.waitKey(1)
                            current_time = time.time()
                            if current_time - start_time >= 3:
                                break
                        if bit is not None:
                            continue
                        else:
                            if color == Color.PINK:
                                pink = False
                            elif color == Color.VIOLET:
                                violet = False
                            elif color == Color.LIGHT_BLUE:
                                light_blue = False
                            elif color == Color.BLUE:
                                blue = False
                            elif color == Color.GREEN:
                                green = False
                            elif color == Color.WHITE:
                                white = False
                            elif color == Color.BLACK:
                                black = False
                            elif color == Color.YELLOW:
                                yellow = False
                            cv2.destroyAllWindows()  
                            break                    
                cv2.imshow("Camera", frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            zustand = zustand.WAIT 
            
        elif zustand == Zustand.VERFOLGEN:
            set_arm_position(ep_arm, ArmPosition.FOLLOW)
            last = False
            while True:
                frame2 = ep_camera.read_cv2_image(strategy="newest")
                person = find_person(frame2, Color.SAFTEY_ORANGE)
                if person is not None:
                    x, y, w, h = person
                    follow2(ep_chassis, frame2, x, y, w, h)
                    print(f"({x}, {y}), {w*h}") 
                else:
                    stop_moving(ep_chassis)
                cv2.imshow("Camera", frame2)

                if cv2.waitKey(1) == ord("q"):
                    break
            break

        elif zustand == Zustand.ABLEGEN:
            # Aufruf der Funktion zum Ablegen des Bits mit dem Servomotor
            pass
        elif zustand == Zustand.AUFNEHEMEN:
            # Aufruf der Funktionen zum Einsammeln und Ablegen des Bits
            pass
            break
        elif zustand == Zustand.WAIT:
            break
    cv2.destroyAllWindows() 
    ep_camera.stop_video_stream()
    print("Finish")
    # Disconnect from the robot
    ep_robot.close()

if __name__ == "__main__":
    main()



