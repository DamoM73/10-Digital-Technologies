from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear

# Define variable
level = 255

while True:
    bearing = sense.get_orientation_degrees()
    #sleep(0.5)
    roll = (round(bearing['roll']))
    pitch = (round(bearing['pitch']))
    yaw = (round(bearing['yaw']))    
    print(f"Roll:{roll} Pitch:{pitch} Yaw:{yaw}")