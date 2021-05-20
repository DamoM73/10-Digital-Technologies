from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

sense.show_letter("M")

while True:
    
    a = sense.get_accelerometer_raw()
    x = a["x"]
    y = a["y"]
    z = a["z"]
    
    x = int(round(x,0))
    y = int(round(y,0))
    z = int(round(z,0))
    
    print(f"X:{x} Y:{y} Z:{z}")
    
    if x == 1:
        sense.set_rotation(270)
    elif x == -1:
        sense.set_rotation(90)
    elif y == -1:
        sense.set_rotation(180)
    else:
        sense.set_rotation(0)