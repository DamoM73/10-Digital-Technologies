from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

while True:
    
    # Get acceleration reading
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    
    # Round acceleration reading
    x = int(round(x,0))
    y = int(round(y, 0))
    z = int(round(z, 0))
    
    print(f"x={x}G, y={y}G, z={z}G")
    