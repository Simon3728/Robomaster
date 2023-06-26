import cv2
from enum import Enum
from driving import rotate_on_spot, stop_moving, drive_forward, Rotation
import threading
import time

# Define an enumeration for the Colors
class Color(Enum):
    # H-Wert, Toleranz, min_S, min_V, max_S, max_V
    SAFTEY_ORANGE = 12, 10, 150, 100, 255, 255
    PINK = 172, 7, 100, 100, 255, 255
    VIOLET = 160, 10, 50, 50, 255, 255
    LIGHT_BLUE = 105, 7, 50, 50, 255, 255
    BLUE = 120, 10, 50, 40, 255, 255
    GREEN = 85, 10, 50, 50, 255, 255
    WHITE = 110, 15, 10, 100, 150, 255
    BLACK = 18, 13, 20, 10, 200, 100
    YELLOW = 37, 8, 150, 100, 255, 255
    

def collect_bit(ep_chassis, frame, x, y, w, h):
    tolerance_x = 20
    tolerance_y = 20
    speed = 15

    frame_center_x = frame.shape[1] // 2
    bit_position_x = x + w/2
    bit_bottom_y = y + h  # Calculate the bottom y-coordinate of the bit
    frame_height = frame.shape[0]
    # Calculate the distance of the bit from the desired position
    distance_x = bit_position_x - frame_center_x
    distance_y = frame_height - bit_bottom_y

    if abs(distance_x) >= tolerance_x:
        #rotation_speed = min(15, int(abs(distance_x) * 0.5)) 
        if distance_x < 0:
            rotate_on_spot(ep_chassis, speed, Rotation.ANTICLOCKWISE)
        else:
            rotate_on_spot(ep_chassis, speed, Rotation.CLOCKWISE)
        print(f"Rotate: {speed}")
    else:
        drive_forward(ep_chassis, speed)
    print(f"(x, y): ({distance_x}, {distance_y})")

    if abs(distance_x) <= tolerance_x and abs(distance_y) <= tolerance_y:
        return True
    return False

def create_mask(hsv, color):
    # Define the lower and upper bounds of the color range in HSV format
    lower = (color.value[0] - color.value[1], color.value[2], color.value[3])
    upper = (color.value[0] + color.value[1], color.value[4], color.value[5])

    # Create a binary mask based on the color range
    mask = cv2.inRange(hsv, lower, upper)
    return mask

def find_bit(frame, color):
    # Convert the frame from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for the specified color
    mask = create_mask(hsv, color)

    # Apply the mask to the frame 
    masked_frame = cv2.bitwise_and(frame, frame, mask=mask)
    #cv2.imshow("Masked Frame", masked_frame)

    # Convert the masked frame to grayscale
    gray = cv2.cvtColor(masked_frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Gray Frame", gray)

    # Apply a binary threshold
    _, binary = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    #cv2.imshow("Binary Frame", binary)

    # Define the threshold for removing the top part
    threshold_y = int((1/3)*frame.shape[0])

    # Set the pixels above the threshold to black
    binary[:threshold_y, :] = 0

    # Set the pixels above the threshold to black in the original frame
    frame[:threshold_y, :] = 0

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        # Calculate the contour area
        area = cv2.contourArea(contour)
        # Check if the contour area is within a certain range
        if area > 250 and area < 4000:
            # Get the bounding rectangle
            x, y, w, h = cv2.boundingRect(contour)

            # Draw the rectangle on the frame
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Return the bounding rectangle coordinates
            return x, y, w, h
    return None


def check_color(pink, violet, light_blue, blue, green, white, black, yellow):
    true_variables = []

    if pink:
        true_variables.append(Color.PINK)
    if violet:
        true_variables.append(Color.VIOLET)
    if light_blue:
        true_variables.append(Color.LIGHT_BLUE)
    if blue:
        true_variables.append(Color.BLUE)
    if green:
        true_variables.append(Color.GREEN)
    if white:
        true_variables.append(Color.WHITE)
    if black:
        true_variables.append(Color.BLACK)
    if yellow:
        true_variables.append(Color.YELLOW)

    return true_variables

