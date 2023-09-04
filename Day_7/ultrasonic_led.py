import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24
LED = 17
BUZZER = 27

print ("Distance Measurement In Progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(BUZZER,GPIO.OUT)

try:
    while True:
        
        GPIO.output(TRIG, False)
        print ("Waiting For Sensor To Settle")
        time.sleep(2)
        
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
        
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
        
        pulse_duration = pulse_end - pulse_start
        
        distance = pulse_duration * 17000
        
        distance = round(distance, 2)
        
        if (distance < 20):
            GPIO.output(LED, GPIO.HIGH)
            GPIO.output(BUZZER, GPIO.HIGH)
        else:
            GPIO.output(LED, GPIO.LOW)
            GPIO.output(BUZZER, GPIO.LOW)
            
        print ("Distance: ",distance,"cm")
        
except KeyboardInterrupt:
    print("Cleaning up!")
    GPIO.cleanup()
finally:
    GPIO.cleanup()
    print("final cleanup")