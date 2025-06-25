from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from controller import TrafficLightSubsystem, PedestrianSubsystem
from time import sleep

led_pedestrian_green = Led_Light(19, False, True)
led_pedestrian_red = Led_Light(17, False, True)

led_traffic_red = Led_Light(3, False, True)
led_traffic_amber = Led_Light(5, False, True)
led_traffic_green = Led_Light(6, False, True)

pedestrian_button = Pedestrian_Button(22, False)
buzzer = Audio_Notification(27, True)
traffic_light = TrafficLightSubsystem(led_traffic_red, led_traffic_amber, led_traffic_green, True)
pedestrian_light = PedestrianSubsystem(led_pedestrian_red, led_pedestrian_green, pedestrian_button, buzzer, True)

def Traffic_Subsystem_Driver():
    print("Testing Traffic Light In 5 Seconds")
    sleep(5)
    traffic_light.show_red()
    print("Pass If: Red ON, Amber OFF, Green OFF")
    sleep(5)
    traffic_light.show_green()
    print("Pass If: Red OFF, Amber OFF, Green ON")
    sleep(5)
    traffic_light.show_amber()
    print("Pass If: Red OFF, Amber ON, Green OFF")
    sleep(5)
    print("Traffic Light Testing Complete")

def Pedestrian_Subsystem_Driver():
    print("Testing Pedestrian Light In 5 Seconds")
    sleep(5)
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
sleep(1)
Pedestrian_Subsystem_Driver()