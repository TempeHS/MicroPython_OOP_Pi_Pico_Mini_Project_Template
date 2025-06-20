from project.lib.led_light import Led_Light
from time import sleep, time

led = Led_Light(3, True, True)

print("Testing on() method")
led.on()
sleep(0.1)
if led.value() == 1:
    print("on() method passed")
else:
    print("on() method failed")

print("Testing off() method")
led.off()
sleep(0.1)
if led.value() == 0:
    print("off() method passed")
else:
    print("off() method failed")

print("Testing toggle() method")
led.toggle()
sleep(0.1)
if led.value() == 1:
    print("toggle() on method passed")
else:
    print("toggle() on method failed")

led.toggle()
sleep(0.1)
if led.value() == 0:
    print("toggle() off method passed")
else:
    print("toggle() off method failed")

print("Testing led_light_state (getter)")
state = led.led_light_state
sleep(0.1)
if state == led.value():
    print("led_light_state (getter) passed")
else:
    print("led_light_state (getter) failed")

print("Testing led_light_state (setter)")
set0 = led.led_light_state = 0
set1 = led.led_light_state = 1
sleep(0.1)
if set1 == 1 and set0 == 0:
    print("led_light_state (setter) passed")
else:
    print("led_light_state (setter) failed")