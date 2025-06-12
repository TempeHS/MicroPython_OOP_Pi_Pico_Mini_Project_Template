from machine import Pin
import time
class Led_Light(Pin):
    # done testing
    def __init__(self, pin, debug=False, flashing=False):
        super().__init__(pin, Pin.OUT)
        self.led_light_state
        self.__debug = debug
        self.__flashing = flashing
        self.__pin = pin
        self.__last_toggle_time = time.time()
        
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
        else:
            raise TypeError("Not the true value")
    
    # done test
    def flash(self):
        now = time.time()
        if self.__flashing and now - self.__last_toggle_time >= 0.5:
            self.toggle()
            self.__last_toggle_time = now

class Pedestrian_Button(Pin):
    def __init__(self, pin, debug = False):
        super().__init__(pin, Pin.IN, Pin.PULL_DOWN)
        self.__debug = debug
        self.__pin = pin
        self.__last_pressed = 0
        self.__pedestrian_waiting = False
        self.button_state
        # set up interrupt on rising edge
        self.irq(trigger=Pin.IRQ_RISING, handler=self.callback)
    
    @property
    def button_state(self):
        if self.__debug:
            print(f"Button connected to Pin {self.__pin} is {"WAITING" if self.__pedestrian_waiting else "NOT WAITING"}")
        return self.__pedestrian_waiting
    
    @button_state.setter
    def button_state(self, value:bool):
        self.__pedestrian_waiting = value
        if self.__debug:
            print(f"Button state on Pin {self.__pin} set to {value}")
    
    def callback(self, pin):
        current_time = time.ticks_ms()
        # 200ms delay
        if (time.ticks_diff(current_time, self.__last_pressed) > 200):
            self.__last_pressed = current_time
            self.__pedestrian_waiting = True
            if self.__debug:
                print(f"Button pressed on Pin {self.__pin} at {current_time}ms")
    