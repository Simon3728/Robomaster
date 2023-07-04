import RPi.GPIO as GPIO
import time

servoPIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)  # GPIO 17 as PWM with 50Hz
p.start(7.5)  # Initialization at the middle position

rotation_time = 0.5  # Time in seconds for one complete rotation (adjust as needed)

try:
    while True:
        position = input("Enter position (1-6): ")
        if position == '1':
            p.ChangeDutyCycle(12.5)  # Full speed clockwise
        elif position == '2':
            p.ChangeDutyCycle(10)  # Medium speed clockwise
        elif position == '3':
            p.ChangeDutyCycle(7.5)  # Stop (middle position)
        elif position == '4':
            p.ChangeDutyCycle(5)  # Medium speed counterclockwise
        elif position == '5':
            p.ChangeDutyCycle(2.5)  # Full speed counterclockwise
        elif position == '6':
            break  # Exit the loop if position 6 is selected
        else:
            print("Invalid position. Please enter a number between 1 and 6.")
            continue

        time.sleep(rotation_time)  # Sleep for the rotation time

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()

