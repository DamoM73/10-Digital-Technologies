from sense_hat import SenseHat

sense = SenseHat()

blue = (0,0,255)
red = (255,0,0)

for num in range(1,6):
    sense.show_message("Pass "+str(num), text_colour=red, back_colour=blue,scroll_speed=0.05)