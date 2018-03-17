import machine
import time

RED    = (100,   0,   0)
GREEN  = (  0, 100,   0)
BLUE   = (  0,   0, 100)
CYAN   = (  0, 100, 100)
YELLOW = (100, 100,   0)
PINK   = (100,   0, 100)
ORANGE = (100,  10,   0)
OFF    = (  0,   0,   0)


class Color():
    """
    Create a multi-color LED control object, using supplied pin numbers for their respective
    colors. Control is achieved by modifying the duty cycle of the LED pin via the PWM module.
    """
    def __init__(self, red_pin, grn_pin, blu_pin):
        try:
            self.LED_RED = machine.PWM(machine.Pin(red_pin, machine.Pin.OUT))
            self.LED_GRN = machine.PWM(machine.Pin(grn_pin, machine.Pin.OUT))
            self.LED_BLU = machine.PWM(machine.Pin(blu_pin, machine.Pin.OUT))
        except Exception as e:
            raise e

    def set(self, rgb=tuple()):
        """
        Takes the values as a percentage of intensity from 1 - 100 for each color and sets them.
        :param rgb: A tuple of values (R, G, B) indicating the intensity of each color, as a
                    percentage from 1 - 100.
        :return: nothing
        """
        self.LED_RED.duty(round(1023 * (rgb[0] / 100)))
        self.LED_GRN.duty(round(1023 * (rgb[1] / 100)))
        self.LED_BLU.duty(round(1023 * (rgb[2] / 100)))

    def cycle_test(self):
        """
        Cycle the colors set as constants above to test function of LED
        :return:
        """
        colors = (RED, GREEN, BLUE, CYAN, YELLOW, PINK, ORANGE, OFF)
        for color in colors:
            self.set(color)
            time.sleep(3)


if __name__ == '__main__':
    try:
        c = Color(26, 25, 27)
        c.cycle_test()
    except:
        pass