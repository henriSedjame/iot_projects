
```python 
from moteur import Motor
from capteur import Sensor
import utime

# On définit une distance
DISTANCE_THRESHOLD = 10

motor = Motor(28)
sensor = Sensor(27, 26)
opened = False


while True:
    distance = sensor.get_distance()

    if distance > 0:
        if not opened and distance < DISTANCE_THRESHOLD:
            print(f'open -> {distance}')
            motor.move(0)
            opened = True
        if opened and distance >= (2 * DISTANCE_THRESHOLD):
            print(f'close -> {distance}')
            motor.move(90)
            opened = False
    if opened:
        utime.sleep(1)
```