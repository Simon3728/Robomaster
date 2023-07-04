import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

servo_channel = 4  # Channel number of the servo

# Set the servo to a specific position
pwm.set_pwm(servo_channel, 0, 100)
time.sleep(5)

# Turn off the servo
pwm.set_pwm(servo_channel, 0, 0)
