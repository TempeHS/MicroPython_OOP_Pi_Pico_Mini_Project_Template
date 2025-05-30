from machine import Pin, PWM, ADC
from time import sleep

# get usb working
sleep(0.1)

led_pin = 25
led2_pin = 15
analog_pin = 26
data_pin = 13

led = PWM(Pin(led_pin))
led2 = PWM(Pin(led2_pin))

led.freq(1000)
led2.freq(1000)

data = Pin(data_pin, Pin.IN)

analog_data = ADC(Pin(analog_pin))

while True:
    adc_value = analog_data.read_u16()
    if data.value() == 1:
        led.duty_u16(adc_value)
        led2.duty_u16(adc_value)
    else:
        led.duty_u16(0)
        led.duty_u16(0)
    print(f"Digital: {data.value()}, Analog: {adc_value}")
    sleep(0.1)