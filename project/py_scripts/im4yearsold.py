from machine import Pin
from time import sleep

class Led_Light(Pin):
    def __init__(self, pin, debug=False, flashing=False):
        super().__init__(pin, Pin.OUT)
        self.__debug = debug
        self.__flashing = flashing
        self.__pin = pin
    
    def on(self):
        self.high()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is on")
    
    def off(self):
        self.low()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is off")
    
    def toggle(self):
        if self.value() == 0:
            self.on()
        elif self.value() == 1:
            self.off()
    
    @property
    def led_light_state(self):
        return self.value()
    
    @led_light_state.setter
    def led_light_state(self, value):
        if value == 0:
            self.off()
        elif value == 1:
            self.on()

red_light = Led_Light(3, True, True)

while True:
    red_light.toggle()
    sleep(0.5)