import RPi.GPIO as GPIO
import os
import sys
import time
push_button = 21
led = 17

import nexmo
client = nexmo.Client(key='xxx', secret='yyy')



def setup():
    GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
    GPIO.setup(led,GPIO.OUT)
    GPIO.setup(push_button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
                    
def destroy():
    GPIO.output(led, GPIO.LOW)     # led off
    
if __name__ == "__main__":     # Program start from here
    setup()
    while(True):
        if(GPIO.input(push_button) == False):
            try:        
                GPIO.output(led,GPIO.HIGH)
                print("sms sent")
                #os.system("python send_sms.py") #Using this line in any python program you can send sms. This call the send_sms.py program and runs it.
                client.send_message({'from': 'Nexmo', 'to': '00917899772828', 'text': 'Hello Raspberry PI world'})
                break
            
            except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
                destroy()
            finally:
                GPIO.cleanup()
                print("clean up completed")
        else:
            print("waiting for user push button action...")
            time.sleep(2)
        
        
                
