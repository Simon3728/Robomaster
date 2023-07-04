import RPi.GPIO as GPIO
import time

servoPIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)  # GPIO 17 as PWM with 50Hz
p.start(2.5)  # Initialization

rotation_time = 2.0  # Time in seconds for one complete rotation (adjust as needed)

try:
    p.ChangeDutyCycle(5)  # Set the duty cycle for the desired position
    time.sleep(rotation_time)  # Sleep for the rotation time
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
