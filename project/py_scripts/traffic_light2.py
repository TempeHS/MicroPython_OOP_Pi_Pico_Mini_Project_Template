from machine import Pin
from time import sleep
import time

class LED_Light(Pin):
    def __init__(self, pin, flashing = False, debug = False):
        self.__pin = pin
        self.__flashing = flashing
        self.__debug = debug
        super().__init__(pin, Pin.OUT)
    
    def on(self):
        self.high()
    
    def off(self):
        self.low()
    
    @property
    def led_light_state(self) -> int:
        return self.value()
    
    @led_light_state.setter
    def led_light_state(self, value):
        if value == 0:
            self.off()
        elif value == 1:
            self.on()
        else:
            raise ValueError("Value has to be 0 or 1, nothing else")
    
    def flash(self, duration:int):
        if self.__debug:
            print(f"Starting flash, duration: {duration}")
        counter = 0
        while True:
            if (counter % duration == 0):
                break
            self.on()
            sleep(0.5)
            self.off()
            sleep(0.5)
            counter+=1
        if self.__debug:
            print("Stopping flash")
    
    def on_for(self, duration:int):
        self.on()
        sleep(duration)
    
class Pedestrian_Button(Pin):
    def __init__(self, pin, debug = False):
        self.__deltatime = time.time_ns
        self.__pin = pin
        self.__debug = debug
        self.__pedestrian_waiting = False
        super().__init__(pin, Pin.IN)
    
    @property
    def button_state(self):
        if self.value == 0:
            return False
        if self.value == 1:
            return True
        raise TypeError("Button state does not exist")
    
    @button_state.setter
    def button_state(self, value:bool):
        if value:
            self.value(1)
        else:
            self.value(0)
    
    