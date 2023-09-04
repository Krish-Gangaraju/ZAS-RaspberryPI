import time
import board
from digitalio import DigitalInOut, Direction
from gpiozero import LED
from time import sleep


import smtplib
import RPi.GPIO as GPIO
import time


led = LED(17)
pad_pin = board.D23

pad = DigitalInOut(pad_pin)
pad.direction = Direction.INPUT

already_pressed = False


  
#Email Variables
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = 'zas.academy.info@gmail.com' #change this to match your gmail account
GMAIL_PASSWORD = 'XXXXXXXXXX'  #change this to match your gmail password
 

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
        
while True:

    if pad.value and not already_pressed:
        print("pressed")
        led.on()
        emailContent = "The sensor was touched at: " + time.ctime()
        sender.sendmail(sendTo, emailSubject, emailContent)
        print("Email Sent")
    else:
        led.off()

    already_pressed = pad.value
    time.sleep(0.1)
