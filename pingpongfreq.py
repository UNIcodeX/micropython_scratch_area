import machine
import time

p14 = machine.Pin(14, machine.Pin.OUT)
p2 = machine.Pin(2, machine.Pin.OUT)


def setPWM(OBJ=None, FREQ=500, DUTY=1023):
    if OBJ is None:
        return None
    # print(OBJ, FREQ, DUTY)
    machine.PWM(OBJ, freq=FREQ, duty=DUTY)


while True:
    for i in range(1, 1024, 1):
        setPWM(OBJ=p2, FREQ=i)
        setPWM(OBJ=p14, FREQ=i)
    # print(i)
    for i in range(1024, 0, -1):
        setPWM(OBJ=p2, FREQ=i)
        setPWM(OBJ=p14, FREQ=i)
    # print(i)
    time.sleep(.7)
