import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

import smtplib

TRIG = 23
ECHO = 24
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

#Email Variables
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = 'roohi0510@gmail.com' #change this to match your gmail account
GMAIL_PASSWORD = 'SanaZara20052010&'  #change this to match your gmail password
 

class Emailer:
    def sendmail(self, recipient, subject, content):
          
        #Create Headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient,
                   "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)
  
        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()
  
        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
  
        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit
  
sender = Emailer()
 


sendTo = 'roohi_fakruddin@yahoo.co.uk'
emailSubject = "Touch Detected!"
emailContent = "The sensor was touched at: " + time.ctime()
        
try:
    while True:
        
        GPIO.output(TRIG, False)
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
        
        print ("Distance: ",distance,"cm")
        
except KeyboardInterrupt:
    print("Cleaning up!")
    GPIO.cleanup()
finally:
    GPIO.cleanup()
    print("final cleanup")
