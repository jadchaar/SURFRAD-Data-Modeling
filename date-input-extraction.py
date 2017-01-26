#!~/anaconda/envs/data_processing/bin/python
from dateutil import parser
import time

while True:
    try:
        dateInput = input('Input a date (MM/DD/YYYY): ')
        dateTime = parser.parse(dateInput, fuzzy=True)
        julianDay = dateTime.timetuple().tm_yday
        year = dateTime.timetuple().tm_year
        print(dateTime)
        print(julianDay)
        print(year)
        break
    except Exception as e:
        print(e, '\nPlease input a valid date.')
        continue
