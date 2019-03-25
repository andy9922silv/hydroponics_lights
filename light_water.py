from datetime import datetime
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

current_time = datetime.now()
print datetime.now()
print current_time.minute
print (current_time.hour-7)

while True:
        if(current_time.minute == 22):
                GPIO.output(8, GPIO.HIGH) # Turn on
                sleep(600) # Sleep for 10 minutes
                GPIO.output(8, GPIO.LOW) # Turn off
                sleep(3600) # Sleep for 1 hour
