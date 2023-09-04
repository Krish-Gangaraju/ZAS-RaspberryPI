import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

led = GPIO.PWM(21, 50)
led.start(0)

while(1):
    for dc in range(0, 101, 5):
        led.ChangeDutyCycle(dc)
        time.sleep(0.1)

    for dc in range(100, -1, -5):
        led.ChangeDutyCycle(dc)
        time.sleep(0.1)
