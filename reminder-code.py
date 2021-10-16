import time

print("What shall I remind you about?: ")
text = str(input())
print("In how many minutes?: ")
local_time = float(input())
print("Reminder set!")
print("We'll notify you at the designated time!")
local_time = local_time * 60
time.sleep(local_time)
print("Alert! You had set reminder for: ", text)
