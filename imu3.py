# imu 3
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

# display character
sense.show_letter("D")

while True:
     # get the acceration reading
     accel = sense.get_accelerometer_raw()
     x = accel['x']
     y = accel['y']
     z = accel['z']
     
     # round readings
     x = int(round(x,0))
     y = int(round(y,0))
     z = int(round(z,0))
     
     print(f"x={x}, y={y}, z={z}")
     
     if x == 1:
         sense.set_rotation(270)
     elif x == -1:
         sense.set_rotation(90)
     elif y == -1:
         sense.set_rotation(180)
     else:
         sense.set_rotation(0)
