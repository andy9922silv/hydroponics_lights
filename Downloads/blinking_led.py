import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

#turns on LED and turns them off after a certain time
#runs on the raspberry pi

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

while True: # Run forever
 GPIO.output(8, GPIO.HIGH) # Turn on
 sleep(28800) # Sleep for 8 hours
 GPIO.output(8, GPIO.LOW) # Turn off
 sleep(57600) # Sleep for 16 hours
