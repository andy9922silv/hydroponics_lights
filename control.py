from datetime import datetime
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on
RELAIS_1_GPIO = 22


current_time = datetime.now()
print datetime.now()
print current_time.minute
print current_time.hour



# if statement works after the first minute of every hour
# pin 17 controls the water pump with the relay control
# pin 8 controls the light

#ph constant check like every minute or 10 times per minute
#bunch of if statements

ph_constant

while True:
        # this if statement checks the time and turns on the lights and the water pump
        if (datetime.now().minute >= 01 and datetime.now().minute <= 50):
                GPIO.output(8, GPIO.HIGH) # Turn on
                GPIO.output(22, GPIO.HIGH) # Turn on
        # this if statement checks the time and turns off the lights and the water pump
        if (datetime.now().minute == 51):
                GPIO.cleanup()
                GPIO.output(8, GPIO.LOW) # Turn off
                GPIO.out(22, GPIO.LOW) # Turn off
        # this if statement checks the time and checks the ph
        if ((datetime.now().minute) % 2 == 0 )
