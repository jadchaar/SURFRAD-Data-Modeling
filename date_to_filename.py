#!~/anaconda/envs/data_processing/bin/python
from dateutil import parser
import json
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

# Convert julian day and year to string
julianDay = str(julianDay)
year = str(year)

if len(julianDay) == 1:
    julianDay = '00' + julianDay
elif len(julianDay) == 2:
    julianDay = '0' + julianDay

# Extract the last two digits of year
year = year[2:]

with open('station-abbreviation-dictionary.json', 'r') as d:
    stationAbbreviations = json.load(d)

while True:
    try:
        location = input('Enter a location: ')
        location = location.title()
        locationEnding = location[-2:].upper()
        wordOne, wordTwo = location.split()[:2]
        location = wordOne + ' ' + wordTwo + ' ' + locationEnding
        print('You entered:', location)
        abbreviation = stationAbbreviations[location]
        break
    except Exception as e:
        print('Please ensure that the location you entered is valid.')
        continue

finalFilename = abbreviation + year + julianDay
print('Final Filename:', finalFilename)
