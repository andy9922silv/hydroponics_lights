from datetime import datetime
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

current_time = datetime.now()

while True:
        if(current_time.minute =10)
        GPIO.output(8, GPIO.HIGH) # Turn on
        sleep(600) # Sleep for 10 minutes
        GPIO.output(8, GPIO.LOW) # Turn off
        sleep(3600) # Sleep for 1 hour
