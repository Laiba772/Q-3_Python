# project 05  countdown timer in python.


import time
import sys

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = f'{mins:02d}:{secs:02d}'
        print(time_format, end='\r', flush=True)  # Ensure real-time updating
        time.sleep(1)
        seconds -= 1
    print("\n00:00 - Time's Up!")    

# User input with error handling
while True:
    try:
        total_seconds = int(input("Enter time in seconds for countdown: "))
        if total_seconds > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

countdown_timer(total_seconds)
