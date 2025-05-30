from machine import Pin, ADC
from time import sleep

sleep(0.1)

led_pin = 25
led2_pin = 15
data_pin = 13
analog_data_pin = 26

led = Pin(led_pin, Pin.OUT)
led2 = Pin(led2_pin, Pin.OUT)

data = Pin(data_pin, Pin.IN)

adc_value = ADC(Pin(analog_data_pin))

while True:
    if data.value() == 1:
        led.value(True)  #turn on the LED
        led2.value(False)  #turn off the LED2
    else:
        led.value(False)  #turn off the LED
        led2.value(True)  #turn on the LED2
    print(print(f"Analog: {adc_value}"))
    sleep(0.1)