import pickle

fullDataNameDictionary = {
    'station_name': 'Station Name',
    'latitude': 'Latitude (degrees)',
    'longitude': 'Longitude (degrees)',
    'elevation': 'Elevation (meters)',
    'year': 'Year',
    'julianDay': 'Julian Day',
    'month': 'Month',
    'day': 'Day',
    'hour': 'Hour',
    'minute': 'Minutes',
    'decimalTime': 'Decimal Time',
    'zenith': 'Solar Zenith Angle (\u00b0)',
    'dwSolar': 'Downwelling Solar Radiation (W/m\u00B2)',
    'uwSolar': 'Upwelling Solar Radiation (W/m\u00B2)',
    'directNormal': 'Direct Normal Solar Radiation (W/m\u00B2)',
    'diffuseSolar': 'Downwelling Diffuse Solar Radiation (W/m\u00B2)',
    'dwInfrared': 'Downwelling Thermal Infrared Solar Radiation (W/m\u00B2)',
    'dwInfraredCaseTemp': 'Downwelling Infrared Case Temperature (K)',
    'dwInfraredDomeTemp': 'Downwelling Infrared Dome Temperature (K)',
    'uwInfrared': 'Upwelling Thermal Infrared Radiation (W/m\u00B2)',
    'uwInfraredCaseTemp': 'Upwelling Infrared Case Temperature',
    'uwInfraredDomeTemp': 'Upwelling Infrared Dome Temperature',
    'ultravioletB': 'Ultraviolet B Radiation (mW/m\u00B2)',
    'photosyntheticActiveRad': 'Photosynthetically Active Radiation (W/m\u00B2)',
    'netSolar': 'Net Solar Radiation (W/m\u00B2)',
    'netInfrared': 'Net Infrared Radiation (W/m\u00B2)',
    'netRadiation': 'Net Solar + Infrared Radiation (W/m\u00B2)',
    'airTemp': '10 meter Air Temperature (\u00b0C)',
    'relativeHumidity': 'Relative Humidity (%)',
    'windSpeed': 'Wind Speed (m/s)',
    'windDirection': 'Wind Direction (\u00b0, clockwise from north)',
    'pressure': 'Station Pressure (mb)'
}

stationNameDictionary = {
    'bon': 'Bondville, IL',
    'fpk': 'Fort Peck, MT',
    'gwn': 'Goodwin Creek, MO',
    'tbl': 'Table Mountain, CO',
    'dra': 'Desert Rock, NV',
    'psu': 'Penn State, PA',
    'sxf': 'Sioux Falls, SD'
}

with open('data-name-dictionary.txt', 'wb') as d:
    pickle.dump(fullDataNameDictionary, d)

with open('station-name-dictionary.txt', 'wb') as d:
    pickle.dump(stationNameDictionary, d)
