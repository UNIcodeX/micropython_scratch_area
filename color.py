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
    def __init__(self, pin_red, pin_grn, pin_blu, debug=False):
        # in case the object has already been instantiated on these pins
        try:
            machine.PWM(machine.Pin(pin_red, machine.Pin.OUT)).deinit()
            machine.PWM(machine.Pin(pin_grn, machine.Pin.OUT)).deinit()
            machine.PWM(machine.Pin(pin_blu, machine.Pin.OUT)).deinit()
        except Exception as e:
            pass

        try:
            self.LED_RED = machine.PWM(machine.Pin(pin_red, machine.Pin.OUT))
            self.LED_GRN = machine.PWM(machine.Pin(pin_grn, machine.Pin.OUT))
            self.LED_BLU = machine.PWM(machine.Pin(pin_blu, machine.Pin.OUT))
        except Exception as e:
            raise e

        self.set_color(OFF)
        self.current = OFF
        self.target  = tuple()
        self.origin  = tuple()
        self.debug   = debug

    def set_color(self, rgb=tuple()):
        """
        Takes the values as a percentage of intensity from 1 - 100 for each color and sets them.
        
        :param rgb: A tuple of values (R, G, B) indicating the intensity of each color, as a
                    percentage from 1 - 100.
        :return: nothing
        """
        self.LED_RED.duty(round(1023 * (rgb[0] / 100)))
        self.LED_GRN.duty(round(1023 * (rgb[1] / 100)))
        self.LED_BLU.duty(round(1023 * (rgb[2] / 100)))
        self.current = rgb

    def transition(self, rgb=tuple(), duration=1):
        """
        Fade from current (R, G, B) value to another.
        
        :param rgb: The (R, G, B) combination, as saturation percentage, to transition to
        :param duration: The time to take to complete the transition
        :return: 
        """
        self.target = rgb
        self.origin = self.current

        origin_red = self.origin[0]
        origin_grn = self.origin[1]
        origin_blu = self.origin[2]

        target_red = self.target[0]
        target_grn = self.target[1]
        target_blu = self.target[2]

        if self.target != self.current:
            self.origin = self.current
            diff_red = target_red - origin_red
            diff_grn = target_grn - origin_grn
            diff_blu = target_blu - origin_blu

            if self.debug:
                print("difference: ", diff_red, diff_grn, diff_blu)

            if diff_red < 0:
                step_red = -1
                diff_red = diff_red * -1
            else:
                step_red = 1

            if diff_grn < 0:
                step_grn = -1
                diff_grn = diff_grn * -1
            else:
                step_grn = 1

            if diff_blu < 0:
                step_blu = -1
                diff_blu = diff_blu * -1
            else:
                step_blu = 1

            diff_largest = max((diff_red, diff_grn, diff_blu))

            if self.debug:
                print('largest diff: ', diff_largest)

            sleep_interval = duration / diff_largest

            if self.debug:
                print("sleep interval is ", str(sleep_interval))

            list_red = [r for r in range(origin_red, target_red, step_red)]
            list_grn = [g for g in range(origin_grn, target_grn, step_grn)]
            list_blu = [b for b in range(origin_blu, target_blu, step_blu)]

            list_red.reverse()
            list_grn.reverse()
            list_blu.reverse()

            if self.debug:
                print('list red:\n', list_red, '\nlist grn:\n', list_grn, '\nlist blu:\n', list_blu)
            
            while (self.current[0], self.current[1], self.current[2]) != (target_red, target_grn, target_blu):
                time.sleep(sleep_interval)
                if list_red:
                    value_red = list_red.pop()
                else:
                    value_red = target_red
                if list_grn:
                    value_grn = list_grn.pop()
                else:
                    value_grn = target_grn
                if list_blu:
                    value_blu = list_blu.pop()
                else:
                    value_blu = target_blu
                self.set_color((value_red, value_grn, value_blu))

    def cycle_test(self):
        """
        Cycle the colors, using the constants above, to test function of LEDs.
        """
        colors = (RED, GREEN, BLUE, CYAN, YELLOW, PINK, ORANGE)
        # Direct setting of color test
        for i in range(1, 3):
            for color in colors:
                self.set_color(color)
                time.sleep(.5)
        # Smooth transition of color test
        for i in range(1, 3):
            for color in colors:
                self.transition(color, duration=2)
        # Turn off the LEDs
        self.transition(OFF)


if __name__ == '__main__':
    try:
        c = Color(26, 25, 27)
        c.cycle_test()
    except:
        pass