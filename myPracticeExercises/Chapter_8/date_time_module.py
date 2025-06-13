# Datetime Module:

#           Classes in datetime:
'''
date:   A naive date, assuming the current Gregorian calendar is in effect. Objects are immutable. 
        Attributes: year, month, and day.


time:   An idealized time, independent of any particular day, assuming that every day has exactly 24*60*60 seconds. 
        Objects can be aware or naive. Objects are immutable.
        Attributes: hour, minute, second, microsecond, and time zone information.


datetime:   A combination of date and a time. Objects can be aware or naive. Objects are immutable.
            Attributes: year, month, day, hour, minute, second, microsecond, and time zone information.


timedelta:  A duration expressing the difference between two date, time, or datetime instances to microsecond resolution.


tzinfo:     An abstract base class for time zone information objects. These are used by the datetime and time classes to 
            provide a customizable notion of time adjustment (for example, to account for time zone and daylight saving time).


timezone:   A class that implements the tzinfo abstract base class as a fixed offset from the UTC. Objects are immutable.
'''

# import datetime

# timestamp_date = datetime.date.fromtimestamp(1682350249)

# print(timestamp_date)       # 2023-04-24

#######################################################################

#*           Date object that represents the current date using the today() method:

# import datetime

# today = datetime.date.today()

# print (today)
# print(today.year)
# print(today.month)
# print(today.day)
# print(today.weekday())        # weekday returns the day of week as a number
                                # Monday  is 0, Tuesday is 1, and so on.

#######################################################################

#           Creating a datetime instance
# import datetime

# now = datetime.datetime.now()
# print (now)         # This is the datetime object
# print (now.year)    # prints only the year from the object
# print (now.month)   # prints only the month from the object
# print (now.day)     # prints only the day, as a number, from the object
# print (now.hour)    # prints only the hour (in UTC time)
# print (now.minute)  # prints only the minute
# print (now.second)  # prints only the second

######################################################################

#           Object that represents a specific day in the past or future

# import datetime

# past_date = datetime.datetime(2015, 3, 14, 9, 26)
# print(past_date)

########################################################################

#           Finding Deltas:
# Finds the duration between two dates by applying the subtraction math operator.

# import datetime

# my_birth_date = datetime.datetime(1920, 11, 17)
# print (my_birth_date)

# current_date = datetime.datetime.now()

# delta = current_date - my_birth_date

# print (delta)

#######################################################################

#       Finding a date in the past or future:

# import datetime

# start_date = datetime.date(2000, 7, 5) # known date
# end_date = start_date + datetime.timedelta(weeks=441) #unknown date

# print(start_date)
# print (end_date)

#######################################################################

#       Converting a string value to a date object:

'''
from datetime import date

new_date_obj = date.fromisoformat('2023-07-15')
print(new_date_obj)
'''

'''
- strptrime() does the same thing as the code above
- strptime()  -> takes two arguments: a date or time string

-   %d  -> day of the month
-   %m  -> month (1-12)
-   %Y  -> year including the century
'''

###########################      EXAMPLE #1:
'''
from datetime import datetime

date_string = "1/1/2000"
date_format = "%m/%d/%Y"

new_date = datetime.strptime(date_string, date_format)
print (new_date)
'''

# from datetime import datetime

# date_in_str = '2005-5-15'
# date_format = '%Y-%m-%d'

# formatted_date = datetime.strptime(date_in_str, date_format)

# print(formatted_date)


##########################       EXAMPLE #2:

# from datetime import datetime

# date_string = "12 May, 2222"
# date_format = "%d %B, %Y"
# new_date = datetime.strptime(date_string, date_format)
# print (f"{date_string} converts to", new_date)


# date_string = "Mar 10 2020 08:27"
# date_format = "%b %d %Y %H:%M"
# new_date = datetime.strptime(date_string, date_format)
# print (f"{date_string} converts to", new_date)

#####################################################################

#       The strftime() method:

#   #############################       EXAMPLE:
'''
# from datetime import datetime

# new_date = datetime(2020, 7, 31)
# print (new_date.strftime("%B"))
# '''

# from datetime import datetime

# new_date = datetime(2015, 3, 30, 10, 30)
# print(new_date.strftime('%A'))

########################################################################

#       CHALLENGE: NEXT FRIDAY

'''
Write a function that takes a date as input and returns the number of days until the 
next Friday.
'''
from datetime import datetime

def date_converter(date):
	date_format = '%m-%d-%Y'

	formatted_date = datetime.strptime(date, date_format)
	# returns the week_day as an int
	# Monday = 0
	week_day = formatted_date.weekday()
	if week_day <= 4:
		num_days = 4 - week_day
	else:
		num_days = 11 - week_day
	return num_days

next_Friday = date_converter('08-02-2023')
print(next_Friday)