import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print ("Distance Measurement In Progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
try:
    while True:he
        
        GPIO.output(TRIG, False)
        time.sleep(2)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)


        
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
        
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()

        distance = 10
        pulse_duration = pulse_end - pulse_start
        speed = pulse_duration * distance
        speed = round(speed, 2)
        
        print ("Speed of Sound: ",speed,"m/s")


        
except KeyboardInterrupt:
    print("Cleaning up!")
    GPIO.cleanup()
finally:
    GPIO.cleanup()
    print("final cleanup")
