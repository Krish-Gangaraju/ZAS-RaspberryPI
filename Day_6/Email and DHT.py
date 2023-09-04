import time
import board
from digitalio import DigitalInOut, Direction
from gpiozero import LED
from time import sleep
import adafruit_dht


import smtplib
import RPi.GPIO as GPIO
import time


led = LED(23)
dhtDevice = adafruit_dht.DHT11(board.D17)

  
#Email Variables
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = 'krishuscan@gmail.com' #change this to match your gmail account
GMAIL_PASSWORD = 'gkkraju28'  #change this to match your gmail password
 

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
 


sendTo = 'krishuscan@gmail.com'
emailSubject = "Above 28 degrees!"
emailContent = "Temp crossed 28: " + time.ctime()

        
while True:
    
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% "
              .format(temperature_f, temperature_c, humidity))
        if(temperature_c > 28):
            led.on()
            emailContent = "The sensor was touched at: " + time.ctime()
            sender.sendmail(sendTo, emailSubject, emailContent)
            print("Email Sent")
        else:
            led.off()

            
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])


    time.sleep(2.0)

    
