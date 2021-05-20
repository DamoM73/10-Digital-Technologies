# imu 4
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

# Define colours
red = (255,0,0)

while True:
     # get the acceration reading
     accel = sense.get_accelerometer_raw()
     x = accel['x']
     y = accel['y']
     z = accel['z']
     
     x = abs(x)
     y = abs(y)
     z = abs(z)
     
     if x > 1 or y > 1 or z > 1:
         sense.show_letter("!",red)
     else:
         sense.clear()