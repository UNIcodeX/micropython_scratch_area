import math
import time
from machine import DAC, Pin

"""
cricket: buffer_size=1001, freq=.0001

"""


def signal_generator(pin=25, buffer_size=100, freq=.1):
    # create a buffer containing a sine-wave
    buf = bytearray(buffer_size)
    for i in range(len(buf)):
        buf[i] = 128 + int(127 * math.sin(2 * math.pi * i / len(buf)))

    # output the sine-wave at 400Hz
    p = Pin(pin, Pin.OUT)
    dac = DAC(p)
    while True:
        for i in buf:
            dac.write(i)
            time.sleep(freq)


if __name__ == '__main__':
    signal_generator()