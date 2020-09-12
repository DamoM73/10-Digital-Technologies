from sense_hat import SenseHat

sense = SenseHat()

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
    
    # Display scrolling message
    sense.show_message(message, scroll_speed = 0.075)