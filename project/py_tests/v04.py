from led_light import Led_Light
from time import sleep, time

led = Led_Light(3, True, False)

print("Testing on() method")
led.on()
sleep(1)
input = print("Type '1' if LED is ON")
if input == "1":
    print("on() method passed")
else:
    print("on() method failed")
sleep(2)

# Testing off() method
print("Testing off() method")
led.off()
sleep(1)
if led.value() == 0:
    print("off() method passed")
else:
    print("off() method failed")
sleep(2)

# Testing toggle() on method
print("Testing toggle() method")
led.toggle()
sleep(1)
if led.value() == 1:
    print("toggle() on method passed")
else:
    print("toggle() on method failed")
sleep(2)

# Testing toggle() off method
led.toggle()
sleep(1)
if led.value() == 0:
    print("toggle() off method passed")
else:
    print("toggle() off method failed")
sleep(2)

# Testing led_light_state getter
print("Testing led_light_state (getter)")
state = led.led_light_state
sleep(1)
if state == led.value():
    print("led_light_state (getter) passed")
else:
    print("led_light_state (getter) failed")
sleep(2)

# Testing led_light_state setter
print("Testing led_light_state (setter)")
set0 = led.led_light_state = 0
set1 = led.led_light_state = 1
sleep(1)
if set1 == 1 and set0 == 0:
    print("led_light_state (setter) passed")
else:
    print("led_light_state (setter) failed")

print("Testing complete")