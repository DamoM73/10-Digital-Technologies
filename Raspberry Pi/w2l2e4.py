from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red = (255,0,0)
yellow = (255,255,0)
green = (0,255,0)
cyan = (0,255,255)
blue = (0,0,255)
magenta = (255,0,255)
black = (0,0,0)
white = (255,255,255)

sense.show_letter("M", red)
sleep(.5)
sense.show_letter("U", yellow)
sleep(.5)
sense.show_letter("R", green)
sleep(.5)
sense.show_letter("T", cyan)
sleep(.5)
sense.show_letter("A", blue)
sleep(.5)
sense.show_letter("G", magenta)
sleep(.5)
sense.show_letter("H", white)
sleep(.5)