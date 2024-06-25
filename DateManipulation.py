from datetime import datetime, timedelta, date

# To get the current date and time, use the now() method:
current_dateTime = datetime.now()
print(current_dateTime)

# To get only the current date:
print(date.today())  # Example output: 2024-06-24

# Creating Specific Dates and Times
specific_datetime = datetime(2023, 12, 25, 15, 30, 0)
print(specific_datetime)  # Output: 2023-12-25 15:30:00

specific_date = date(2023, 12, 25)
print(specific_date)  # Output: 2023-12-25

# Formatting Dates and Times
formatted_datetime = current_dateTime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)  # Example output: 2023-06-24 12:34:56

formatted_date = current_dateTime.strftime("%B %d, %Y")
print(formatted_date)  # Example output: June 24, 2023

# Parsing Dates and Times from Strings
date_string = "2023-06-24 12:34:56"
parsed_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(parsed_datetime)  # Output: 2023-06-24 12:34:56


# Adding and Subtracting Time
# Adding 10 days
future_date = current_dateTime + timedelta(days=10)
print(future_date)  # Example output: 2024-07-04

# Subtracting 2 hours
past_datetime = current_dateTime - timedelta(hours=2)
print(past_datetime)  # Example output: 2024-06-24 10:34:56.789123


# Calculating the Difference Between Dates
date1 = date(2024, 6, 24)
date2 = date(2024, 7, 4)
difference = date2 - date1
print(difference)  # Output: 10 days, 0:00:00
print(difference.days)  # Output: 10

# Getting Components of Dates and Times
print(current_dateTime.year)  # Output: 2023
print(current_dateTime.month)  # Output: 6
print(current_dateTime.day)  # Output: 24
print(current_dateTime.hour)  # Output: 12
print(current_dateTime.minute)  # Output: 34
print(current_dateTime.second)  # Output: 56
