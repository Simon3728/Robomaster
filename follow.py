import cv2
from enum import Enum
from driving import rotate_on_spot, stop_moving, drive_forward, drive_backward, Rotation
from getBit import create_mask


def find_person(frame, color):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = create_mask(hsv, color)

    masked_frame = cv2.bitwise_and(frame, frame, mask=mask)
    gray = cv2.cvtColor(masked_frame, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    threshold_y = int((5/6)*frame.shape[0])
    binary[threshold_y:, :] = 0
    frame[threshold_y:, :] = 0
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        # Calculate the contour area
        area = cv2.contourArea(contour)
        if area > 1000 and area < 20000:
            # Get the bounding rectangle
            x, y, w, h = cv2.boundingRect(contour)
            # Draw the rectangle on the frame
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Return the bounding rectangle coordinates or perform additional processing
            return x, y, w, h
    return None

def follow(ep_chassis, frame, x, y, w, h):
    tolerance_x = 200
    tolerance_y = 50
    min_speed = 15
    max_speed = 50
    min_rotation_seep = 15
    max_rotation_speed = 25

    frame_center_x = frame.shape[1] // 2
    person_position_x = x + w/2   # current x position
    person_position_y = y - h  # Calculate the top y-coordinate of the bit

    # Calculate the x-Distance to the person
    distance_x = person_position_x - frame_center_x
    
    normalized_distance = y / ((5/6) * frame.shape[0])
    speed = int(min_speed + (max_speed - min_speed) * normalized_distance)

    if distance_x <= 0:
        rotation_speed = int((-1) * min_rotation_seep + (distance_x / frame_center_x) * (max_rotation_speed - min_rotation_seep))
    else:
        rotation_speed = int(min_speed + (distance_x / frame_center_x) * (max_speed - min_speed))

    w1_speed=speed - rotation_speed
    w2_speed=speed + rotation_speed
    w3_speed=speed + rotation_speed
    w4_speed=speed - rotation_speed

    if w1_speed < 15:
        if w1_speed >= 10:
            w1_speed = -15
    if w2_speed < 15:
        w2_speed = -15
    if w3_speed < 15:
        w3_speed = -15
    if w4_speed < 15:
        w4_speed = -15

    print(w1_speed, w2_speed, w3_speed, w4_speed)
    if w1_speed >= 50:
         w1_speed = 50
    elif w2_speed >= 50:
        w2_speed = 50
    elif w3_speed >= 50:
        w3_speed = 50
    elif w4_speed >= 50:
        w4_speed = 50
    ep_chassis.drive_wheels(w1=w1_speed, w2=w2_speed, w3=w3_speed, w4=w1_speed)

    # if abs(distance_x) >= tolerance_x:
    #     #rotation_speed = min(15, int(abs(distance_x) * 0.5)) 
    #     if distance_x < 0:
    #         rotate_on_spot(ep_chassis, speed, Rotation.ANTICLOCKWISE)
    #     else:
    #         rotate_on_spot(ep_chassis, speed, Rotation.CLOCKWISE)
    #     print(f"Rotate: {speed}")
    # else:
    #     normalized_distance = person_position_y / 500
    #     speed = min_speed + (max_speed - min_speed) * normalized_distance

    #     drive_forward(ep_chassis, speed)

    if abs(distance_x) <= tolerance_x and abs(person_position_y) <= tolerance_y:
        return True
    return False

def follow2(ep_chassis, frame, x, y, w, h):
    tolerance_x = 100
    tolerance_y = 60
    min_speed = 15
    min_rotation_speed = 15
    max_rotation_speed = 35
    max_speed = 100
    frame_center_x = frame.shape[1] // 2
    person_position_x = x + w/2

    # Distance from Person to x-Axis center
    distance_x = person_position_x - frame_center_x

    if abs(distance_x) >= tolerance_x:
        if distance_x < 0:
            rotation_speed = int(min_rotation_speed + ((-1) * distance_x / frame_center_x) * (max_rotation_speed - min_rotation_speed))
            rotate_on_spot(ep_chassis, rotation_speed, Rotation.ANTICLOCKWISE)
        else:
            rotation_speed = int(min_speed + (distance_x / frame_center_x) * (max_speed - min_speed))
            rotate_on_spot(ep_chassis, rotation_speed, Rotation.CLOCKWISE)
        print(f"Rotation Speed: {rotation_speed}")
    else:
        if y < 200:
            normalized_distance = 2* (y / 250)
            speed = int(min_speed + (max_speed - min_speed) * normalized_distance)
            drive_backward(ep_chassis, speed)
        elif y > 300:
            normalized_distance = y / ((5/6) * frame.shape[0])
            speed = int(min_speed + (max_speed - min_speed) * normalized_distance)
            drive_forward(ep_chassis, speed)
        else:
            stop_moving(ep_chassis)
       
    print(f"(x, y): ({distance_x}, {y})")
