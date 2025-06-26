from pedestrian_button import Pedestrian_Button
from time import time, ticks_ms, ticks_diff, sleep

button = Pedestrian_Button(22, True)

# Testing callback() method
print("Testing callback() method")
button.callback(22)
sleep(1)
if button.__pedestrian_waiting == True:
    print("callback() method passed")
else:
    print("callback() method failed")

# Testing button_state getter
print("Testing button_state (getter)")
button.button_state()
sleep(1)
if button.__pedestrian_waiting == True:
    print("button_state (getter) passed")
else:
    print("button_state (getter) failed")

# Testing button_state setter
print("Testing button_state (setter)")
set0 = button.button_state = 0
set1 = button.button_state = 1
sleep(1)
if set0 == 0 and set1 == 1:
    print("button_state (setter) passed")
else:
    print("button_state (setter) failed")