from capteur import Sensor
from pompe import Pump
from time import sleep

sensor = Sensor(26, 70)
pump = Pump(1)

while True:

    if sensor.is_water_detected():
        pump.off()
        sleep(2)
    else:
        pump.on()
        sleep(1)