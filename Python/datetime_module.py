from datetime import datetime
birthday = datetime(1993, 10, 1, 4, 24) # My birthday in year, month, day, hour, minute
birthday.year # will return 1993
birthday.weekday() # will return 4, for Friday
datetime.now() # returns current date and time
datetime(2018, 1, 1) - datetime(2016, 1, 1) # returns datetime.timedelta(720)

datetime.strptime("Jan 14 2005", "https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior")
