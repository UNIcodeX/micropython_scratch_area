import machine
import time
p14 = machine.Pin(14, machine.Pin.OUT)
p2 = machine.Pin(2, machine.Pin.OUT)

direction = 'forward'
forward = [i for i in range(2, 1024)]
backward = [i for i in reversed(forward)]

def setPWM(OBJ=None, FREQ=500, DUTY=1023):
	if OBJ is None:
		return None
	# print(OBJ, FREQ, DUTY)
	machine.PWM(OBJ, freq=FREQ, duty=DUTY)

while True:
	if direction == 'forward':
		for i in forward:
			if i == forward[-1]:
				direction = 'backward'
			setPWM(OBJ=p2, DUTY=i)
			setPWM(OBJ=p14, DUTY=i)
			# print(i)
	elif direction == 'backward':
		for i in backward:
			if i == backward[-1]:
				direction = 'forward'
			setPWM(OBJ=p2, DUTY=i)
			setPWM(OBJ=p14, DUTY=i)
			# print(i)
	time.sleep(.05)