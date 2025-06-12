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

import datetime

# timestamp_date = datetime.date.fromtimestamp(1682350249)

# print(timestamp_date)       # 2023-04-24

#######################################################################

#*           Date object that represents the current date using the today() method:

# import datetime

today = datetime.date.today()

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

my_birth_date = datetime.datetime(1920, 11, 17)
print (my_birth_date)

current_date = datetime.datetime.now()

delta = current_date - my_birth_date

print (delta)

#######################################################################

