from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

white = (255,255,255)

x = 4
y = 4

while True:
    
    # if joystick event detected
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            
            # adjust cordinates
            if event.direction == 'up':
                y = y -1
            elif event.direction == 'down':
                y = y + 1
            elif event.direction == 'right':
                x = x + 1
            elif event.direction == 'left':
                x = x - 1
        
        # check the coords are within the matrix
        if y > 7:
            y = 7
        elif y < 0:
            y = 0
        
        if x > 7:
            x = 7
        elif x < 0:
            x = 0
            
        # redraw pixel
        sense.clear()
        sense.set_pixel(x,y,white)
