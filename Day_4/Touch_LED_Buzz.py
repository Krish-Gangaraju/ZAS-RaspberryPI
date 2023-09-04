import time
import board
from digitalio import DigitalInOut, Direction
from gpiozero import LED
from time import sleep

led_pin = LED(27)
buzzer_pin = board.D17
pad_pin = board.D23

pad = DigitalInOut(pad_pin)
pad.direction = Direction.INPUT
buzzer = DigitalInOut(buzzer_pin)
buzzer.direction = Direction.OUTPUT

alreadybuzz_pressed = False
alreadyled_pressed = False


while True:
    if pad.value and not alreadybuzz_pressed:
        print("pressed")
        buzzer.value = True
        led_pin.on()
    else:
        buzzer.value = False
        led_pin.off()

    alreadybuzz_pressed = pad.value
    alreadyled_pressed = pad.value
    time.sleep(0.1)
