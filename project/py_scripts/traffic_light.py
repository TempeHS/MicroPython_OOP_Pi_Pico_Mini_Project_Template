from machine import Pin
from time import sleep

class Traffic:
    def __init__(self, red_pin:int, yellow_pin:int, green_pin:int):
        self.red = Pin(red_pin, Pin.OUT)
        self.yellow = Pin(yellow_pin, Pin.OUT)
        self.green = Pin(green_pin, Pin.OUT)
        
        self.red.value(True)
        self.green.value(False)
        self.yellow.value(False)
        
    def set_value(self, colour:str, value:bool):
        if colour == 'r':
            self.red.value(value)
        elif colour == 'g':
            self.green.value(value)
        elif colour == 'y':
            self.yellow.value(value)
        else:
            raise Exception("Dude input something you idiot")
    
    def go(self):
        self.set_value('r', False)
        self.set_value('g', True)
    
    def halt(self):
        self.set_value('g', False)
        self.set_value('y', True)
        sleep(3)
        self.set_value('y', False)
        self.set_value('r', True)

class Pedestrian:
    def __init__(self, red_pin:int, green_pin:int, button:int, buzzer:int):
        self.red = Pin(red_pin, Pin.OUT)
        self.green = Pin(green_pin, Pin.OUT)
        
    def set_value(self, colour:str, value:bool):
        if colour == 'r':
            self.red.value(value)
        elif colour == 'g':
            self.green.value(value)
        else:
            raise Exception("Dude input something you idiot")


def main():
    traffic_light = Traffic(green_pin=13, yellow_pin=10, red_pin=8)
    while True:
        traffic_light.go()
        sleep(5)
        traffic_light.halt()
        sleep(5)

main()