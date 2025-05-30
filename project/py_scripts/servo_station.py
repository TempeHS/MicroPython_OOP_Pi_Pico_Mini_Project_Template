from machine import Pin, ADC, PWM
from time import sleep

sleep(0.1)

led_pin = 15
data_pin = 13
analog_data_pin = 26
servo_pin = 10

led = PWM(Pin(led_pin))

led.freq(1000)

servo = PWM(Pin(servo_pin))

servo.freq(50)

data = Pin(data_pin, Pin.IN)

analog_data = ADC(Pin(analog_data_pin))

#function to calculate pulse width in microseconds
def set_angle(angle):
    #clamps the input angle to the range 0–180
    angle = min(max(angle, 0), 180)
    #return PWM mapping 0° to 500 µs and 180° to 2500 µs (standard for many servos).
    return int(500 + (angle / 180) * 2000)


#function to linearly map values
def map_range(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


while True:
    adc_value = analog_data.read_u16()
    if data.value() == 1:
        led.duty_u16(adc_value)
    else:
        led.duty_u16(0)
    mapped_value = map_range(adc_value, 0, 65535, 0, 180)
    servo.duty_ns(set_angle(mapped_value)*1000)
    print(f"Digital: {data.value()} , Analog: {adc_value} , Servo: {servo.duty_ns()}")
    sleep(0.1)