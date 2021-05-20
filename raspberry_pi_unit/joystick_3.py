from sense_hat import SenseHat

sense = SenseHat()

# Define the functions
def red():
    sense.clear(255,0,0)
    
def blue():
    sense.clear(0,0,255)
    
def green():
    sense.clear(0,255,0)
    
def yellow():
    sense.clear(255,255,0)
    
# associate each function with an event
sense.stick.direction_up = red
sense.stick.direction_down = blue
sense.stick.direction_left = yellow
sense.stick.direction_right = green

while True:
    pass # this keeps the program running