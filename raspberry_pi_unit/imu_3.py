from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

# Diplay the letter J
sense.show_letter("J")

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
    
    # Update the rotation of the display
    if x == 1:
        sense.set_rotation(270)
    elif x == -1:
        sense.set_rotation(90)
    elif y == -1:
        sense.set_rotation(180)
    else:
        sense.set_rotation(0)
    