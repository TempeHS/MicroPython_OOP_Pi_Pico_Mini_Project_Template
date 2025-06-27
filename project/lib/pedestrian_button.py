from machine import Pin
from time import time, ticks_ms, ticks_diff 

class Pedestrian_Button(Pin):
    # Child class inherits the parent "Pin" class
    def __init__(self, pin, debug):
        super().__init__(pin, Pin.IN, Pin.PULL_DOWN)
        self.__debug = debug
        self.__pin = pin
        self.__last_pressed = 0 # Tracks the last time the button was pressed
        self.__pedestrian_waiting = False
        # Sets up interrupt on rising edge
        self.irq(trigger=Pin.IRQ_RISING, handler=self.callback)

    def button_state(self, value=None):
        if value is None:
            if self.__debug:
                print(f"Button connected to Pin {self.__pin} is {'WAITING' if self.__pedestrian_waiting else 'NOT WAITING'}")
            return self.__pedestrian_waiting
        else:
            self.__pedestrian_waiting = bool(value) # Convert to boolean to ensure proper type
            if self.__debug:
                print(f"Button state on Pin {self.__pin} set to {value}")

    def callback(self, pin):
        current_time = ticks_ms() # Get the current time in milliseconds
        if (time.ticks_diff(current_time, self.__last_pressed) > 200): # 200ms debounce delay
            self.__last_pressed = current_time
            self.__pedestrian_waiting = True
            if self.__debug:
                print(f"Button pressed on Pin {self.__pin} at {current_time}ms")