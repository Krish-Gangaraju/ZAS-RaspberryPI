import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)


LED = 17
BUZZER = 27

GPIO.setup(LED,GPIO.OUT)
GPIO.setup(BUZZER,GPIO.OUT)

while True:
    GPIO.output(LED, GPIO.HIGH)
    GPIO.output(BUZZER, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(LED, GPIO.LOW)
    GPIO.output(BUZZER, GPIO.LOW)
    time.sleep(5)