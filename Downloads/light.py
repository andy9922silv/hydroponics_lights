from datetime import datetime
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

#using python the hour and minute in real life is extracted
#the LED turns on after it hits the correct time
#will make it turn on for 8-10 hours and turn it off the rest of the time



GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)




current_time = datetime.now()
print(str(current_time))

if (current_time.hour >= 9 and current_time.minute >=0):
    while True: # Run forever
     GPIO.output(8, GPIO.HIGH) # Turn on
     sleep(15) # Sleep for 15 seconds
     GPIO.output(8, GPIO.LOW) # Turn off
     sleep(5) # Sleep for 5 seconds

else:
    print ("It is before 9:00")
