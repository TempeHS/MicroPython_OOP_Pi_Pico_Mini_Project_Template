from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from controller import TrafficLightSubsystem, PedestrianSubsystem, Controller
from time import sleep

# Pedestrian Lights
led_ped_green = Led_Light(19, False, True)
led_ped_red = Led_Light(17, False, True)

# Traffic Lights
led_traffic_red = Led_Light(3, False, True)
led_traffic_amber = Led_Light(5, False, True)
led_traffic_green = Led_Light(6, False, True)

button = Pedestrian_Button(22, False)
buzzer = Audio_Notification(27, True)
controller = Controller(led_ped_red, led_ped_green, led_traffic_red, led_traffic_amber, led_traffic_green, button, buzzer, True)
traffic_light = TrafficLightSubsystem(led_traffic_red, led_traffic_amber, led_traffic_green, True)
pedestrian_light = PedestrianSubsystem(led_ped_red, led_ped_green, button, buzzer, True)

# Testing IDLE state
print("Testing IDLE State")
controller.set_idle_state()
sleep(1)
print("Pass If: Traffic GREEN, Ped RED, Buzzer OFF")
sleep(3)

# Testing CAHNGE state
print("Testing CHANGE State")
controller.set_change_state()
sleep(1)
print("Pass If: Traffic AMBER, Ped RED, Buzzer OFF")
sleep(3)

# Testing WALK state
print("Testing WALK State")
controller.set_walk_state()
sleep(1)
print("Pass If: Traffic RED, Ped GREEN, Buzzer ON")
sleep(3)

# Testing WARNING state
print("Testing WARNING State")
controller.set_warning_state()
sleep(1)
print("Pass If: Traffic RED, Ped FLASHING RED, Buzzer OFF")
sleep(3)

# Testing ERROR state
print("Testing ERROR State")
controller.set_error_state()
sleep(1)
print("Pass If: Traffic AMBER, Ped FLASHING RED, Buzzer OFF")
sleep(3)