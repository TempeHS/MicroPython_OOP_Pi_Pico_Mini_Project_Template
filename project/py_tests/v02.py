from machine import Pin
from machine import PWM

led_car_red = Pin(3, Pin.OUT)
led_car_orange = Pin(5, Pin.OUT)
led_car_green = Pin(6, Pin.OUT)

led_ped_red = Pin(19, Pin.OUT)
led_ped_green = Pin(17, Pin.OUT)

pedestrian_button = Pin(22, Pin.IN, Pin.PULL_DOWN)

buzzer = PWM(27)
buzzer.freq(1000)

while True:
    buzzer.duty_u16(32768)

    led_car_red.on()
    led_car_orange.on()
    led_car_green.on()

    led_ped_red.on()
    led_ped_green.on()

    print(pedestrian_button.value())