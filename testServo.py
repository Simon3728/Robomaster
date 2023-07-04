import RPi.GPIO as GPIO
import time

servoPIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 5)  # GPIO 17 as PWM with 50Hz
p.start(0)  # Initialization

rotation_time = 0.5  # Time in seconds for one complete rotation (adjust as needed)
initial_delay = 2.0  # Time in seconds for initial delay (adjust as needed)
speed = 0.5
try:
    # Wait for the servo to reach its starting position
    time.sleep(initial_delay)
    
    while True:
        position = input("Enter position (1-6): ")
        if position == '1':
            p.ChangeDutyCycle(8)  # Full speed clockwise
            time.sleep(2.5 * rotation_time)
            p.ChangeDutyCycle(0)  # Stop
        elif position == '2':
            p.ChangeDutyCycle(7)  # Medium speed clockwise
            time.sleep(1.5 * rotation_time)
            p.ChangeDutyCycle(0)  # Stop
        elif position == '3':
            p.ChangeDutyCycle(6)  # Medium speed clockwise
            time.sleep(0.5 * rotation_time)
            p.ChangeDutyCycle(0)  # Stop
        elif position == '4':
            p.ChangeDutyCycle(5)
            time.sleep(0.5 * rotation_time)
            p.ChangeDutyCycle(0)  # Stop
        elif position == '5':
            p.ChangeDutyCycle(4)
            time.sleep(1.5 * rotation_time)
            p.ChangeDutyCycle(0)  # Stop
        elif position == '6':
            p.ChangeDutyCycle(3)
            time.sleep(2.5 * rotation_time)
            p.ChangeDutyCycle(0)  # Stop
        elif position == '7':
            break  # Exit the loop if position 6 is selected
        else:
            print("Invalid position. Please enter a number between 1 and 6.")
            continue

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()



