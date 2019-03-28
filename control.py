from datetime import datetime
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
RELAIS_1_GPIO = 22


current_time = datetime.now()
print datetime.now()
print current_time.minute
print (current_time.hour-7)


# if statement works after the first minute of every hour
# pin 17 controls the water pump with the relay control
# pin 8 controls the light

while True:
        if (datetime.now().minute == 33):
                GPIO.output(8, GPIO.HIGH) # Turn on
                sleep(2400) # Sleep for 40 minutes
                GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
                GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
                GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on
                time.sleep(0.25)
                GPIO.output(22, GPIO.HIGH)
                GPIO.cleanup()
                GPIO.output(8, GPIO.LOW) # Turn off
                sleep(1140) # Sleep for 19 minutes
        else: 
                print datetime.now().minute
