import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

LED = 17
BUTTON = 27

GPIO.setup(LED,GPIO.OUT)
GPIO.setup(BUTTON,GPIO.IN)

try: 
    while True:
        if(GPIO.input(BUTTON) == True):
            print("BUTTON NOT PRESSED")
            GPIO.output(LED, GPIO.LOW)
            time.sleep(1)
        else:
            print("BUTTON PRESSED")
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(1)
            
except (KeyboardInterrupt, RuntimeError, TypeError):
    GPIO.cleanup()
    print("clean up performed")
finally:
    GPIO.cleanup()
    print("final cleanup") 