from time import sleep
import stepper_motor
import button
import led

motor = stepper_motor.StepperMotor()
btn = button.Button(16)
green_led = led.LED(18)
red_led = led.LED(22)

green_led.set_intensity(0)
red_led.set_intensity(255)

toggled = False

while True:
    try:
        if btn.tap_button():
            toggled = not toggled
            green_led.set_intensity(255 if toggled else 0)
            red_led.set_intensity(0 if toggled else 255)

            # Sleep is necessary to prevent multiple button presses
            sleep(0.25)
        elif toggled:
            motor.do_clockwise_degrees(1)
    except KeyboardInterrupt:
        motor.clean_up_gpio()
        green_led.clean_up_gpio()
        red_led.clean_up_gpio()
        break
