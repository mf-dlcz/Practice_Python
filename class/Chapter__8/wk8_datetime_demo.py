import datetime

today = datetime.date.today()

# print (today)
# print(today.year)
# print(today.month)
# print(today.day)
# print(today.weekday()) 
## weekday returns the day of week as a number
## Monday  is 0, Tuesday is 1, and so on. 
                       

now = datetime.datetime.now()

# print (now)  # This is the datetime object
# print (now.year) # prints only the year from the object
# print (now.month) # prints only the month from the object
# print (now.day) # prints only the day, as a number, from the object
# print (now.hour) # prints only the hour (in UTC time)
# print (now.minute) # prints only the minute
# print (now.second) # prints only the second

# delta
# date format (year, month, day, hour, minute, second)
# thousand = datetime.timedelta(days=1000)
# new_date = old_date + thousand
past_date = datetime.datetime(2015, 3, 14, 9, 26)
# print (past_date)
current_date = datetime.datetime.now()
delta = current_date - past_date
# print (delta)

# from datetime import datetime

date_string = "1/1/2000"
date_format = "%m/%d/%Y"

new_date = datetime.datetime.strptime(date_string, date_format)
# print (new_date)


# strptime strftime
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

# date_string = "12 May, 2222"
# date_format = "" #FILL THIS IN
# new_date = datetime.datetime.strptime(date_string, date_format)
# print (f"{date_string} converts to", new_date)


# date_string = "Mar 10 2020 08:27"
# date_format = "" #FILL THIS IN
# new_date = datetime.datetime.strptime(date_string, date_format)
# print (f"{date_string} converts to", new_date)