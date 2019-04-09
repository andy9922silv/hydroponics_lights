from datetime import datetime
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setmode(GPIO.BOARD)

current_time = datetime.now()
print datetime.now()
print current_time.minute
print current_time.hour


while True:
    minute = datetime.now().minute
    hour = datetime.now().hour
    if (minute % 2 == 0)
        GPIO.output(8, GPIO.HIGH) # Turn on
    if (minute % 2 == 1)
        GPIO.cleanup()
        GPIO.output(8, GPIO.LOW) # Turn off

    time.sleep(2)
