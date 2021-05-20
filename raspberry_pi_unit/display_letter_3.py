from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

red = (255,0,0)
yellow = (255,255,0)
green = (0,255,0)
cyan = (0,255,255)
blue = (0,0,255)
magenta = (255,0,255)
black = (0,0,0)
white = (255,255,255)

# Generate random colour
def pick_random_colour():
    random_red = randint(0,255)
    random_green = randint(0,255)
    random_blue = randint(0,255)
    return (random_red, random_green, random_blue)

sense.show_letter("M", pick_random_colour())
sleep(.5)
sense.show_letter("U", pick_random_colour())
sleep(.5)
sense.show_letter("R", pick_random_colour())
sleep(.5)
sense.show_letter("T", pick_random_colour())
sleep(.5)
sense.show_letter("A", pick_random_colour())
sleep(.5)
sense.show_letter("G", pick_random_colour())
sleep(.5)
sense.show_letter("H", pick_random_colour())
sleep(.5)

sense.clear()


