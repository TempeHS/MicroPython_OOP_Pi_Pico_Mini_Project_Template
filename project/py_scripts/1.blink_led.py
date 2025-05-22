from machine import Pin
from time import sleep

sleep(0.1)

led_pin = 25

led = Pin(led_pin, pin_OUT)

while True:
    led.value(True)
    time.sleep(1)
    led.value(False)
    time.sleep(1)