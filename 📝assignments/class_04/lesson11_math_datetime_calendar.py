
# Lesson 11: Math, DateTime & Calendar


# Math Module Examples
import math
print("PI value:", math.pi)
print("Power calculation (2^3):", math.pow(2, 3))
print("Square root of 25:", math.sqrt(25))
print("Floor value of 4.7:", math.floor(4.7))
print("Ceiling value of 4.7:", math.ceil(4.7))
print("Factorial of 5:", math.factorial(5))







# DateTime Module Examples
from datetime import datetime, timedelta

current_time = datetime.now()
print("\nCurrent date and time:", current_time)

future_date = current_time + timedelta(days=7)
print("Date after 7 days:", future_date)

past_date = current_time - timedelta(days=7)
print("Date before 7 days:", past_date)

formatted_date = current_time.strftime("%d/%m/%Y, %H:%M:%S")
print("Formatted date and time:", formatted_date)







# Calendar Module Examples
import calendar

print("\nIs 2024 a leap year?:", calendar.isleap(2024))
print("\nWeekday of 1st Jan 2024:", calendar.weekday(2024, 1, 1))

print("\nCalendar for January 2024:")
print(calendar.month(2024, 1))

print("\nCalendar for full year 2024:")
print(calendar.calendar(2024))
