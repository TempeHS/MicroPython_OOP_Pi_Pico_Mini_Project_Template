from machine import Pin
from time import sleep, time

class Led_Light(Pin):
    # done testing
    def __init__(self, pin, debug=False, flashing=False):
        super().__init__(pin, Pin.OUT)
        self.led_light_state
        self.__debug = debug
        self.__flashing = flashing
        self.__pin = pin
        self.__last_toggle_time = time()
        
        if self.__debug:
            print(f"LED Light at pin {self.__pin} has been initialised")
    
    # done testing
    def on(self):
        self.high()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is {self.led_light_state}")
            print("Expected: on")
    
    # done testing
    def off(self):
        self.low()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is {self.led_light_state}")
            print("Expected: off")
    
    # done testing
    def toggle(self):
        if self.value() == 0:
            self.on()
        elif self.value() == 1:
            self.off()
    
    # done test
    @property
    def led_light_state(self):
        return self.value()
    
    # done test
    @led_light_state.setter
    def led_light_state(self, value):
        if value == 0:
            self.off()
        elif value == 1:
            self.on()
    
    # done test
    def flash(self):
        now = time()
        if self.__flashing and now - self.__last_toggle_time >= 0.5:
            self.toggle()
            self.__last_toggle_time = now