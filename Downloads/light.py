from datetime import datetime
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)




current_time = datetime.now()
print(str(current_time))

if (current_time.hour >= 9 and current_time.minute >=56):
    while True: # Run forever
     GPIO.output(8, GPIO.HIGH) # Turn on
     sleep(2) # Sleep for 2 seconds
     GPIO.output(8, GPIO.LOW) # Turn off
     sleep(5) # Sleep for 5 seconds

else:
    print ("It is before 9:56")
