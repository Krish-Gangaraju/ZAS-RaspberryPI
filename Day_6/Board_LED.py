import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)


LED = 11
BUZZER = 13

GPIO.setup(LED,GPIO.OUT)
GPIO.setup(BUZZER,GPIO.OUT)

try: 
    while True:
        GPIO.output(LED, GPIO.HIGH)
        GPIO.output(BUZZER, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(LED, GPIO.LOW)
        GPIO.output(BUZZER, GPIO.LOW)
        time.sleep(5)
except (KeyboardInterrupt, RuntimeError, TypeError):
    GPIO.cleanup()
    print("clean up performed")
finally:
    GPIO.cleanup()
    #GPIO.output(LED, GPIO.LOW)
    #GPIO.output(BUZZER, GPIO.LOW)
    print("final cleanup")
    