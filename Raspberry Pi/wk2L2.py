from sense_hat import SenseHat

sense = SenseHat()

blue = (0,0,255)
red = (255,0,0)

sense.show_message("Hello World!", text_colour=red, back_colour=blue,scroll_speed=1)
