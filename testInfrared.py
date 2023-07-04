import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
sensor_pin = 18  # Beispiel-Pin, passe ihn entsprechend deiner Verbindung an
GPIO.setup(sensor_pin, GPIO.IN)

try:
    while True:
        if GPIO.input(sensor_pin):
            print("Objekt erkannt")
        else:
            print("Kein Objekt erkannt")
        time.sleep(0.1)  # Pause zwischen den Messungen
except KeyboardInterrupt:
    GPIO.cleanup()