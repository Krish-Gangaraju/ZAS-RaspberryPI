import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

LED = 11
BUZZER = 13
TOUCH = 16

GPIO.setup(LED,GPIO.OUT)
GPIO.setup(BUZZER,GPIO.OUT)
GPIO.setup(TOUCH,GPIO.IN)

try:
    while True:
        if (GPIO.input(TOUCH) == True):
            print("Touched")
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(1)
        else:
            print("Not Touched")
            GPIO.output(LED, GPIO.LOW)
            time.sleep(1)
            
except (KeyboardInterrupt, RuntimeError, TypeError):
    GPIO.cleanup()
    print("clean up performed")
finally:
    GPIO.cleanup()
    print("final cleanup") 