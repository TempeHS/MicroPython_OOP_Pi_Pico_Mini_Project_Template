from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from controller import TrafficLightSubsystem, PedestrianSubsystem, Controller
from time import sleep, time

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
controller = Controller(led_ped_red, led_ped_green, led_traffic_red, led_traffic_amber, led_traffic_green, button, buzzer, debug)

# Unit Testing
state = controller.state
last_change = controller.last_state_change
time_now = time()

if state == "IDLE":
    print("State: IDLE")
    if pedestrian_light.is_button_pressed():
        state = "CHANGE"
        last_change = time_now
elif state == "CHANGE":
    print("State: CHANGE")
    if last_change - time_now >= 5:
        controller.set_walk_state()
        state = "WALK"
        last_change = time_now

elif state == "WALK":
    print("State: WALK")
    if last_change - time_now >= 5:
        controller.set_warning_state()
        state = "WARNING"
        last_change = time_now

elif state == "WARNING":
    print("State: WARNING")
    if last_change - time_now >= 5:
        controller.set_idle_state()
        state = "IDLE"
        last_change = time_now

else:
    state = "ERROR"
    controller.set_error_state()
    print("State: ERROR")