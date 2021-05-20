# imu 2
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

while True:
     # get the acceration reading
     accel = sense.get_accelerometer_raw()
     x = accel['x']
     y = accel['y']
     z = accel['z']
     
     #round readings
     x = int(round(x,0))
     y = int(round(y,0))
     z = int(round(z,0))
     
     print(f"x={x}, y={y}, z={z}")
     