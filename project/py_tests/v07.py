from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from controller import TrafficLightSubsystem, PedestrianSubsystem
from time import sleep

debug = False

# Pedestrian Lights
led_ped_red = Led_Light(19, False, debug)
led_ped_green = Led_Light(17, False, debug)

# Traffic Lights
led_traffic_red = Led_Light(3, False, debug)
led_traffic_amber = Led_Light(5, False, debug)
led_traffic_green = Led_Light(6, False, debug)

# Systems
button = Pedestrian_Button(22, debug)
buzzer = Audio_Notification(27, debug)
traffic_light = TrafficLightSubsystem(led_traffic_red, led_traffic_amber, led_traffic_green, debug)
pedestrian_light = PedestrianSubsystem(led_ped_red, led_ped_green, button, buzzer, debug)

def Traffic_Subsystem_Driver():
    print("Testing Traffic Light")
    sleep(2)
    traffic_light.show_red()
    print("Pass If: Red ON, Amber OFF, Green OFF")
    sleep(5)
    traffic_light.show_amber()
    print("Pass If: Red OFF, Amber ON, Green OFF")
    sleep(5)
    traffic_light.show_green()
    print("Pass If: Red OFF, Amber OFF, Green ON")
    sleep(5)
    print("Traffic Light Testing Complete")

def Pedestrian_Subsystem_Driver():
    print("Testing Pedestrian Light")
    sleep(2)
    pedestrian_light.show_stop()
    print("Pass If: Red ON, Green OFF, Buzzer WARNING_OFF")
    sleep(5)
    pedestrian_light.show_walk()
    print("Pass If: Red OFF, Green ON, Buzzer WARNING_ON")
    sleep(5)
    pedestrian_light.show_warning()
    print("Pass If: Red FLASH, Green OFF, Buzzer WARNING_OFF")
    sleep(5)
    print("Pedestrian Light Testing Complete")

Traffic_Subsystem_Driver()
sleep(2)
Pedestrian_Subsystem_Driver()
print("Testing Complete")