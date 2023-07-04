import RPi.GPIO as GPIO
import time

servoPIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)  # GPIO 17 as PWM with 50Hz
p.start(2.5)  # Initialization

rotation_time = 2.0  # Time in seconds for one complete rotation (adjust as needed)

try:
    p.ChangeDutyCycle(3)  # Set the duty cycle for the desired position
    time.sleep(rotation_time)  # Sleep for the rotation time
    p.ChangeDutyCycle(2.5)
    time.sleep(rotation_time)
    p.ChangeDutyCycle(10)  # Set the duty cycle for the desired position
    time.sleep(rotation_time)  # Sleep for the rotation time
    p.ChangeDutyCycle(2.5)
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
