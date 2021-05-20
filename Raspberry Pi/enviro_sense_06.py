from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

red = (255,0,0)
green = (0,255,0)

while True:
    # take reading from the all three sensors
    temp = sense.get_temperature()
    press = sense.get_pressure()
    hum = sense.get_humidity()
    
    # round the values to one decimal place
    temp = round(temp,1)
    press = round(press,1)
    hum = round(hum,1)
    
    # create temp message
    message = "Temp: " + str(temp)
    
    if temp > 18 and temp < 27:
        bg = green
    else:
        bg = red
    
    # Display temp message
    sense.show_message(message, scroll_speed = 0.075, back_colour = bg)
    
    # create pressure a message
    message = " Pressure: " + str(press)
    
    if press > 979 and temp < 1027:
        bg = green
    else:
        bg = red
    
    # Display message
    sense.show_message(message, scroll_speed = 0.075, back_colour = bg)
    
    # create Humidty message
    message = " Humidity: " + str(hum)
    
    if hum > 55 and temp < 65:
        bg = green
    else:
        bg = red
    
    # Display message
    sense.show_message(message, scroll_speed = 0.075, back_colour = bg)
    
    
    