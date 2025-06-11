import fuckall
from time import sleep

def test():
    # firstly get it to initialise
    red_light = fuckall.Led_Light(3, True, False)
    # check using pin val
    assert isinstance(red_light, fuckall.Led_Light), "class aint initialised"
    
    # next get it to turn on
    red_light.on()
    assert red_light.led_light_state == 1, "its not on"
    sleep(1)
    
    # get it to turn off
    red_light.off()
    assert red_light.led_light_state == 0, "its not off"
    sleep(1)
    
    counter = 0
    previous_state = red_light.led_light_state
    while counter < 10:
        red_light.flash()
        assert red_light != previous_state, f"not previous state: {previous_state}"
        counter+=1
    
    previous_state = red_light.led_light_state
    # manually set value
    red_light.toggle()
    assert red_light != previous_state, "did not toggle properly"
    sleep(1)
    # manually set value
    red_light.toggle()
    assert red_light == previous_state, "did not toggle properly"
    sleep(1)
    
    isCaptured = False
    try:
        red_light.led_light_state(0.5)
        assert isCaptured, "Failed to raise exception at invalid value"
    except Exception:
        isCaptured = True
        assert isCaptured
    
    red_light.led_light_state(1)
    assert red_light.led_light_state == 1, "Failed to get led light state"

test()