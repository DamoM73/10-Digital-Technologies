from sense_hat import SenseHat

sense = SenseHat()

# Define colours
red = (255,0,0)
green = (0,255,0)

while True:
    
    # Take readings from all three sensors
    temp = sense.get_temperature()
    press = sense.get_pressure()
    hum = sense.get_humidity()
    
    # Round the values to one deciomal point
    temp = round(temp,1)
    press = round(press,1)
    hum = round(hum,1)
    
    # Create the message
    message = "Temperature: " + str(temp) + " Pressure: " + str(press) + " Humidity: " + str(hum)
    
    if temp > 18.3 and temp < 26.7:
        bg = green
    else:
        bg = red
    
    # Display scrolling message
    sense.show_message(message, scroll_speed = 0.075, back_colour = bg)