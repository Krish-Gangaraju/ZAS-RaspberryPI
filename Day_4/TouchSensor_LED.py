import time
import board
from digitalio import DigitalInOut, Direction
from gpiozero import LED
from time import sleep

led = LED(17)
pad_pin = board.D23

pad = DigitalInOut(pad_pin)
pad.direction = Direction.INPUT

already_pressed = False

while True:

    if pad.value and not already_pressed:
        print("pressed")
        led.on()
    else:
        led.off()

    already_pressed = pad.value
    time.sleep(0.1)
