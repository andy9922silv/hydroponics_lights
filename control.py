from datetime import datetime
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setmode(GPIO.BOARD)

current_time = datetime.now()
print datetime.now()
print current_time.minute
print (current_time.hour-8)



# if statement works after the first minute of every hour
# pin 3 controls the water pump with the relay control
# pin 19 controls the light

#ph constant check like every minute or 10 times per minute
#bunch of if statements    

ph_constant = 2
wp_constant = 4
wp_for = 45



while True:
    minute = datetime.now().minute
    hour = datetime.now().hour
    # this if statement checks the time and turns on the lights for 15 hours
    if(hour >= 01 and minute <= 00):
        GPIO.output(19, GPIO.HIGH) # Turn on
    # this if statement checks the time and turns on or off the pump
    if(hour % 2 == 0 and minute <= 40):
        GPIO.output(3, GPIO.HIGH) # Turn on
    else:
        GPIO.output(3, GPIO.LOW) # Turn off
    # this if statement checks the time and turns off the lights
    if(hour >= 17):
        GPIO.output(19, GPIO.LOW) # Turn off

    # this if statement checks the time and checks the ph
    if(hour %  ph_constant == 0):
        pass
        
    # this if statement checks the time and pumps the water
    if(minute % wp_constant == 0 and minute < wp_for ):
        pass

    #time.sleep(2) # sleeps for 2 seconds
