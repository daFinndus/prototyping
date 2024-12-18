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
            sleep(0.15)
        elif toggled:
            motor.run_as_fast_as_it_can()
    except KeyboardInterrupt:
        print("KeyboardInterrupt detected. Exiting...")
        break
    except Exception as e:
        print("Error in main loop: " + e)
        break
