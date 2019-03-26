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
        if(current_time.minute == 0):
                print "test"
                GPIO.output(8, GPIO.HIGH) # Turn on
                sleep(2400) # Sleep for 40 minutes
                GPIO.output(8, GPIO.LOW) # Turn off
                sleep(1140) # Sleep for 19 minutes 
                
