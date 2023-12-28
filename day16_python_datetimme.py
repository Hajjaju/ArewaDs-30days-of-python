#EXERCISES: Day 16

from datetime import datetime

# Question 1:Get the current day, month, year, hour, minute and 
# timestamp from datetime module
current = datetime.now()
current_day = current.day
current_month = current.month
current_year = current.year
current_hour = current.hour
current_minute = current.minute
current_timestamp = current.timestamp()

print(current_year, current_month, current_day, current_hour, current_minute, current_timestamp)

# Question 2: Format the current date using this format: 
# "%m/%d/%Y, %H:%M:%S")
formatted_current_Date = current.strftime("%m/%d/%Y, %H:%M:%S")
print(formatted_current_Date)

# Question 3: Today is 5 December, 2019. Change this 
# time string to time.
today = datetime(year=2019, month = 12, day = 5)
print(today)

# Question 4: Calculate the time difference between now and new year.
new_year = datetime(year=2024, month=1, day=1, minute=0, second=0)
diff = new_year - current
print(f"The time difference between now and new year is: {diff}")

# Question 5: Calculate the time difference between 1 January 1970 and now.
past_year = datetime(year=1970, month=1, day=1)
diff = current - past_year
print(f"The time difference betwween now and 1970 is: {diff}")

# Question 6: Think, what can you use the datetime module for? Examples:
    # Time series analysis
    # To get a timestamp of any activities in an application
    # Adding posts on a blog
 # Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime

now = datetime.now()

current_day = now.day
current_month = now.month
current_year = now.year
current_hour = now.hour
current_minute = now.minute
timestamp = now.timestamp()

print(f"Current Day: {current_day}")
print(f"Current Month: {current_month}")
print(f"Current Year: {current_year}")
print(f"Current Hour: {current_hour}")
print(f"Current Minute: {current_minute}")
print(f"Timestamp: {timestamp}")

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Formatted Date: {formatted_date}")

# Today is 5 December, 2019. Change this time string to time.
time_string = "5 December, 2019"
converted_time = datetime.strptime(time_string, "%d %B, %Y")
print(f"Converted Time: {converted_time}")

# Calculate the time difference between now and new year.
from datetime import timedelta

new_year = datetime(now.year + 1, 1, 1)
time_difference_to_new_year = new_year - now

print(f"Time difference to New Year: {time_difference_to_new_year}")

# Calculate the time difference between 1 January 1970 and now.
epoch_time = datetime(1970, 1, 1)
time_difference_to_epoch = now - epoch_time

print(f"Time difference to 1 January 1970: {time_difference_to_epoch}")

# Think, what can you use the datetime module for? Examples:
# Time series analysis
# To get a timestamp of any activities in an application
# Adding posts on a blog   