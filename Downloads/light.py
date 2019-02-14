from datetime import datetime


current_time = datetime.now()
print(str(current_time))

if (current_time.hour >= 9 and current_time.minute >=42):
    print("It is after 9:42")

else:
    print ("It is before 9:42")
