from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

while True:
    o = sense.get_orientation()

    #print(o)

    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]

    print(f"Pitch:{pitch}  Roll:{roll}  Yaw:{yaw}")
