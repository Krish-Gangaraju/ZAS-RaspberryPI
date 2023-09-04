import RPi.GPIO as GPIO
import os
import sys
push_button = 23
led = 18

import nexmo
client = nexmo.Client(key='YOUR-API-KEY', secret='YOUR-API-SECRET')



def setup():
        GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
        GPIO.setup(led,GPIO.OUT)
        GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
                    
def destroy():
        GPIO.output(17, GPIO.LOW)     # led off
if _name_ == "_main_":     # Program start from here
        setup()
        try:
                if(GPIO.input(push_button) == True):
                        GPIO.output(18,GPIO.HIGH)
                        print("sms sent")
						#os.system("python send_sms.py") #Using this line in any python program you can send sms. This call the send_sms.py program and runs it.
						client.send_message({'from': 'Nexmo', 'to': 'YOUR-PHONE-NUMBER', 'text': 'Hello world'})
			break				              		
		
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
                destroy()
				


