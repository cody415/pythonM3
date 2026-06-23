import datetime
import calendar

# Program to display all month names

# Get current year (not strictly needed, but useful for context)
year = datetime.datetime.now().year

print(f"Months of the year {year}:")

# Loop through 1 to 12 for months
for month in range(1, 13):
    print(calendar.month_name[month])
