from sense_hat import SenseHat

sense = SenseHat()

# Define Colours
g = (0,255,0) # Green
b = (0,0,0) # Black

# setup where each colour will display
image_pixel = [
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,b,b,g,g,b,b,g,
    g,b,b,g,g,b,b,g,
    g,g,g,b,b,g,g,g,
    g,g,b,b,b,b,g,g,
    g,g,b,b,b,b,g,g,
    g,g,b,g,g,b,g,g
]

# Display on matrix
sense.set_pixels(image_pixel)