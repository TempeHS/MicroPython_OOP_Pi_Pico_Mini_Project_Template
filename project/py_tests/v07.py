from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from controller import TrafficLightSubsystem, PedestrianSubsystem
from time import sleep

led_pedestrian_red = Led_Light(19, False, True)
led_pedestrian_red = Led_Light(17, False, True)
led_traffic_red = Led_Light(3, False, True)
led_traffic_amber = Led_Light(5, False, True)
led_traffic_green = Led_Light(6, False, True)
pedestrian_button = Pedestrian_Button(22, True)
buzzer = Audio_Notification(27, True)

def Subsystem_Driver():
    print("Testing")