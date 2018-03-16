import machine
from encoder import Encoder
import uasyncio as asyncio


async def set_val(val):
    print('setting value to ' + str(val))


async def monitor():
    enc = Encoder(4, 5, clicks=4, min_val=0, max_val=255)
    lastval = enc.value

    while True:
        val = enc.value
        if lastval != val:
            lastval = val
            await set_val(val)

        enc.cur_accel = max(0, enc.cur_accel - enc.accel)
        await asyncio.sleep(.1)


loop = asyncio.get_event_loop()
loop.run_until_complete(monitor())
