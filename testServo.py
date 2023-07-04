import RPi.GPIO as GPIO
import time

servoPIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 20)  # GPIO 17 as PWM with 50Hz
p.start(0)  # Initialization

rotation_time = 0.5  # Time in seconds for one complete rotation (adjust as needed)
initial_delay = 2.0  # Time in seconds for initial delay (adjust as needed)
speed = 0.5
try:
    # Wait for the servo to reach its starting position
    time.sleep(initial_delay)
    i = 2
    while True:
        p.ChangeDutyCycle(i)
        print(i)
        time.sleep(2)
        i += 0.1
        if i >= 3:
            break

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()



