import json
import sys


def form_dict():
    fullDataNameDictionary = {
        'stationName': 'Station Name',
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

    fullDataNameDictionaryReversed = {
        'Station Name': 'station_name',
        'Longitude': 'longitude',
        'Wind Speed': 'windSpeed',
        'Wind Direction': 'windDirection',
        'Net Solar Radiation': 'netSolar',
        'Downwelling Infrared Case Temperature': 'dwInfraredCaseTemp',
        'Upwelling Thermal Infrared Radiation': 'uwInfrared',
        'Upwelling Infrared Dome Temperature': 'uwInfraredDomeTemp',
        'Year': 'year',
        'Solar Zenith Angle': 'zenith',
        'Photosynthetically Active Radiation': 'photosyntheticActiveRad',
        'Julian Day': 'julianDay',
        'Upwelling Infrared Case Temperature': 'uwInfraredCaseTemp',
        'Downwelling Infrared Dome Temperature': 'dwInfraredDomeTemp',
        '10 meter Air Temperature': 'airTemp',
        'Day': 'day',
        'Net Solar + Infrared Radiation': 'netRadiation',
        'Net Infrared Radiation': 'netInfrared',
        'Station Pressure': 'pressure',
        'Downwelling Diffuse Solar Radiation': 'diffuseSolar',
        'Downwelling Thermal Infrared Solar Radiation': 'dwInfrared',
        'Direct Normal Solar Radiation': 'directNormal',
        'Hour': 'hour',
        'Minutes': 'minute',
        'Upwelling Solar Radiation': 'uwSolar',
        'Elevation': 'elevation',
        'Month': 'month', 'Downwelling Solar Radiation': 'dwSolar',
        'Latitude': 'latitude',
        'Relative Humidity': 'relativeHumidity',
        'Ultraviolet B Radiation': 'ultravioletB',
        'Decimal Time': 'decimalTime'
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

    stationAbbreviationDictionary = {
        'Bondville, IL': 'bon',
        'Bondville IL': 'bon',
        'Bondville': 'bon',
        'Fort Peck, MT': 'fpk',
        'Fort Peck MT': 'fpk',
        'Fort Peck': 'fpk',
        'Goodwin Creek, MO': 'gwn',
        'Goodwin Creek MO': 'gwn',
        'Goodwin Creek': 'gwn',
        'Table Mountain, CO': 'tbl',
        'Table Mountain CO': 'tbl',
        'Table Mountain': 'tbl',
        'Desert Rock, NV': 'dra',
        'Desert Rock NV': 'dra',
        'Desert Rock': 'dra',
        'Penn State, PA': 'psu',
        'Penn State PA': 'psu',
        'Penn State': 'psu',
        'Sioux Falls, SD': 'sxf',
        'Sioux Falls SD': 'sxf',
        'Sioux Falls SD': 'sxf'
    }

    try:
        with open('data-name-dictionary.json', 'w') as d:
            json.dump(fullDataNameDictionary, d, ensure_ascii=False)

        with open('data-name-dictionary-reversed.json', 'w') as d:
            json.dump(fullDataNameDictionaryReversed, d, ensure_ascii=False)

        with open('station-name-dictionary.json', 'w') as d:
            json.dump(stationNameDictionary, d, ensure_ascii=False)

        with open('station-abbreviation-dictionary.json', 'w') as d:
            json.dump(stationAbbreviationDictionary, d, ensure_ascii=False)
    except Exception as e:
        print(e)
        sys.exit(1)
