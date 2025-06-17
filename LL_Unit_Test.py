from led_light import Led_Light
from time import sleep

led = Led_Light()(3, flashing=True, debug=True)

print("Testing on()")
led.on()
if led.value == 1:
    print("On() passed")
sleep(0.1)

print("Testing off()")
led.off()
if led.value == 0:
    print("Off() passed")

print("Testing toggle()")
led.toggle()
if led.value == 1:
    print("toggle() on passed")
sleep(0.1)
if led.value == 0:
    print("toggle() off passed")

sleep(1)
if led.value = 0:
    print("toggle()")