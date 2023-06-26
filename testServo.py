import RPi.GPIO as GPIO
import time

servo_pin = 18  # GPIO pin number where the servo is connected

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

servo_pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz (20 ms period)

def set_speed(speed):
    if speed < 0:
        servo_pwm.ChangeDutyCycle(0)  # Stop rotating
    else:
        duty_cycle = speed * 2 + 6  # Map speed (-1 to 1) to duty cycle (4-10%)
        servo_pwm.ChangeDutyCycle(duty_cycle)

try:
    while True:
        speed = float(input("Enter the desired speed (-1 to 1, q to quit): "))
        if speed < -1 or speed > 1:
            print("Invalid speed. Please enter a value between -1 and 1.")
            continue
        if speed == 'q':
            break
        set_speed(speed)

except KeyboardInterrupt:
    pass

servo_pwm.stop()
GPIO.cleanup()
