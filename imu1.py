# imu 1 
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

o = sense.get_orientation()
pitch = o["pitch"]
roll = o["roll"]
yaw = o["yaw"]

print(f"pitch:{pitch} roll:{roll} yaw:{yaw}")