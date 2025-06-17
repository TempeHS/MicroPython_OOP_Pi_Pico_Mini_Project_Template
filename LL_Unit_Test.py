from led_light import Led_Light
from time import sleep, time

led = Led_Light(3, True, True)

# Testing on()
print("Testing on() method")
led.on()
sleep(0.1)
if led.value() == 1:
    print("on() method passed")
else:
    print("on() method failed")

# Testing off()
print("Testing off() method")
led.off()
sleep(0.1)
if led.value() == 0:
    print("off() method passed")
else:
    print("off() method failed")

# Testing toggle()
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

# Testing led_light_state() getter
print("Testing led_light_state() getter")