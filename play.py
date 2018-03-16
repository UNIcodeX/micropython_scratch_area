import wave
from machine import Pin, DAC
from time import sleep_ms


def play(filename, pin):
    try:
        p = Pin(pin, Pin.OUT)
        dac = DAC(p)
    except Exception as e:
        return str(e)
    f = wave.open(filename, 'r')
    total_frames = f.getnframes()
    framerate = f.getframerate()

    for position in range(0, total_frames, framerate):
        f.setpos(position)
        # dac.write_timed(f.readframes(framerate), framerate)
        dac.write(f.readframes(framerate))
        sleep_ms(1000)
