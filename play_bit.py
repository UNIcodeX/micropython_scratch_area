import machine, time

p = machine.Pin(25, machine.Pin.OUT)
dac = machine.DAC(p)

with open('tron_bit_yes_8bit_w.wav', 'rb') as f:
    buf = f.read()

for i in buf:
    dac.write(i)
    time.sleep(.001)

dac.write(0)
