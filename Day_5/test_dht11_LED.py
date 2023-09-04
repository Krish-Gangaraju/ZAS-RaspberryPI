import time
import board
import adafruit_dht
from gpiozero import LED
from time import sleep

led= LED(27)
# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D17)

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% "
              .format(temperature_f, temperature_c, humidity))
        if(temperature_c > 26):
            led.on()
        else:
            led.off()

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])

    time.sleep(2.0)
