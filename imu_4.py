from sense_hat import SenseHat

sense = SenseHat()

# Define Colours
red = (255,0,0)
green = (0,255,0)

while True:
    # Get readings
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    
    x = abs(x)
    y = abs(y)
    z = abs(z)
    
    if x > 1 or y > 1 or z > 1:
        sense.show_letter("!", red)
    else:
        sense.clear()
    