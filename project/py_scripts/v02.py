from machine import Pin
from time import sleep

# Wait for USB to become ready
sleep(0.1)

# Store desired output pin in a variable
led_pin = 25
led2_pin = 15
data_pin = 13

# Configure GPIO Pin as an output pin and create an led object for Pin class
led = Pin(led_pin, Pin.OUT)
led2 = Pin(led2_pin, Pin.OUT)

# Configure GPIO Pin as an input pin and create a data object for Pin class
data = Pin(data_pin, Pin.IN)

while True:
    if data.value() == 1:
        led.value(True)
        led2.value(False)
    else:
        led.value(False)
        led2.value(True)
    sleep(0.1)