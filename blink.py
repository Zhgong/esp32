import machine
import time

led = machine.Pin(2, machine.Pin.OUT)

print("start")

for i in range(10):
    time.sleep(1)
    led.on()
    time.sleep(1)
    led.off()
print("stop")
    