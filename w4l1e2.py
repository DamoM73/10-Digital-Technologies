from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

while True:
    
    a = sense.get_accelerometer_raw()
    x = a["x"]
    y = a["y"]
    z = a["z"]
    
    x = int(round(x,0))
    y = int(round(y,0))
    z = int(round(z,0))
    
    print(f"X:{x} Y:{y} Z:{z}")