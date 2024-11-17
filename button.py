from RPi import GPIO


class Button:
    def __init__(self, pin):
        # Create dictionary stor
        self.pin = pin

        # Set the GPIO mode to BOARD and set up the pin as an output
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.IN)

        print(f"Setup for pin {self.pin} is complete.")
        print(f"Setup for the button is completed.\n")

    # Function to check if button 1 is being pressed
    def tap_button(self):
        if GPIO.input(self.pin) == GPIO.LOW:
            print(f"Button {self.pin} is pressed.")
            return True
        else:
            return False
