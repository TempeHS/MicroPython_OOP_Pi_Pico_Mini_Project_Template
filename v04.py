from led_light import Led_Light
from time import sleep

red_light = Led_Light(25, True, True)

while True:
    print(red_light.led_light_state)
    red_light.led_light_state = 1
    sleep(1)
    print(red_light.led_light_state)
    red_light.led_light_state = 0
    sleep(1)