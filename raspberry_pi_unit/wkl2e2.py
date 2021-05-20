from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

while True:
    for event in sense.stick.get_events():
        
        # Check if joystick is pressed
        if event.action == 'pressed':
            
            # check which direction has been pressed
            if event.direction == 'up':
                sense.show_letter('U')
            elif event.direction == 'down':
                sense.show_letter('D')
            elif event.direction == 'left':
                sense.show_letter('L')
            elif event.direction == 'right':
                sense.show_letter('R')
            elif event.direction == 'middle':
                sense.show_letter('M')
        elif event.action == 'released':
            sense.clear()
                
            