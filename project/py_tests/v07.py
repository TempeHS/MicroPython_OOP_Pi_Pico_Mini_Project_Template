from project.lib.led_light import Led_Light
from project.lib.pedestrian_button import Pedestrian_Button
from project.lib.audio_notification import Audio_Notification
from project.lib.controller import TrafficLightSubsystem, PedestrianSubsystem
from time import sleep

led_pedestrian_red = Led_Light(19, False, True)
led_pedestrian_red = Led_Light(17, False, True)

led_traffic_red = Led_Light(3, False, True)
led_traffic_amber = Led_Light(5, False, True)
led_traffic_green = Led_Light(6, False, True)

pedestrian_button = Pedestrian_Button(22, True)
buzzer = Audio_Notification(27, True)
traffic_light = TrafficLightSubsystem(led_traffic_red, led_traffic_amber, led_traffic_green, True)

def Traffic_Subsystem_Driver():
    print("Testing Traffic Light In 5 Seconds")
    sleep(5)
    traffic_light.show_red()
    print("Pass If: Red ON, Amber OFF, Green OFF")
    sleep(10)
    traffic_light.show_green()
    print("Pass If: Red OFF, Amber OFF, Green ON")
    sleep(10)
    traffic_light.show_amber()
    print("Pass If: Red OFF, Amber ON, Green OFF")
    sleep(10)
    print("Traffic Light Testing Complete")