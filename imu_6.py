from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear

# Define variable
white = (255,255,255)

x = 4
y = 4

while True:
    o = sense.get_orientation_radians()
    pitch = o["pitch"]
    roll = o["roll"]
    
    x_move = round(pitch*10)*-1
    y_move = round(roll*10)
    print(x_move,y_move)
    
    x += x_move
    y += y_move
    
    if x > 7:
        x = 7
    elif x < 0:
        x = 0
        
    if y > 7:
        y = 7
    elif y < 0:
        y = 0
        
    sense.clear()
    sense.set_pixel(x,y,white)
    sleep(0.2)
    
    