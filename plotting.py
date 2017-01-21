#!~/anaconda/envs/plotting/bin/python
import configparser
import os
import pickle
import plotly
# input plotly username and API key
plotly_info = configparser.ConfigParser()
plotly_info.read('config.ini')
plotly_username = plotly_info.get('PlotlyInfo', 'username')
plotly_api_key = plotly_info.get('PlotlyInfo', 'api_key')
plotly.tools.set_credentials_file(
    username=plotly_username, api_key=plotly_api_key)
plotly.tools.set_config_file(world_readable=True, sharing='public')
import plotly.plotly as py
from plotly.graph_objs import *  # noqa: H303


def plot_graph():
    print('\n### DATA PLOTTING PROGRAM ###\n')
    print('Step 3. Choose data to plot')
    print('\nListing available data files for plotting...\n')

    originalPath = os.getcwd()
    os.chdir(os.getcwd() + '/ftp_files')
    print('## Data ##\n', *os.listdir(os.getcwd()), sep=' | ', end=' |\n')

    # fileToRead = input('\nEnter a data file to read: ')
    while True:
        try:
            fileToRead = str(input('\nEnter a data file to read: '))
        except ValueError:
            print('Error: Please input a valid filename!')
            continue

        if fileToRead == '':
            print('Error: Please input a valid filename!')
            continue
        elif fileToRead[-4:] != '.dat':
            if len(fileToRead) == 8:
                print('\n', fileToRead, 'valid! Reading...')
                break
            else:
                print('Error: Please input a valid filename!')
                continue

        elif fileToRead[-4:] == '.dat':
            if len(fileToRead) == 12:
                print('\n', fileToRead, 'valid! Reading...')
                break
            else:
                print('Error: Please input a valid filename!')
                continue
        else:
            print('\n', fileToRead, 'valid! Reading...')
            break

    if fileToRead[(len(fileToRead) - 4):len(fileToRead)] != '.dat':
        fileToRead += '.dat'

    # print('\nReading', fileToRead, '...')

    # with open('psu17001.dat', 'r') as f:
    with open(fileToRead, 'r') as f:
        stationName = f.readline().strip()
        secondLine = f.readline().strip()
        dataArray = []
        # next(f)
        # next(f)
        for line in f:
            dataArray.append([float(x) for x in line.split()])
        f.close()

    # Extract data from second line
    latitude, longitude, elevation = secondLine.split()[:3]
    elevation = elevation.replace(" m version 1", "")
    latitude = float(latitude)
    longitude = float(longitude)
    elevation = int(elevation)

    plottingOptions = ['year', 'julianDay', 'month', 'day', 'hour', 'minute',
                       'decimalTime', 'zenith', 'dwSolar', 'uwSolar',
                       'directNormal', 'diffuseSolar', 'dwInfrared',
                       'dwInfraredCaseTemp', 'dwInfraredDomeTemp',
                       'uwInfrared', 'uwInfraredCaseTemp',
                       'uwInfraredDomeTemp', 'ultravioletB',
                       'photosyntheticActiveRad', 'netSolar', 'netInfrared',
                       'netRadiation', 'airTemp', 'relativeHumidity',
                       'windSpeed', 'windDirection', 'pressure']

    # year = [int(x[0]) for x in dataArray]
    # julianDay = [int(x[1]) for x in dataArray]
    # month = [int(x[2]) for x in dataArray]
    # day = [int(x[3]) for x in dataArray]
    # hour = [int(x[4]) for x in dataArray]
    # minute = [int(x[5]) for x in dataArray]«»
    decimalTime = [float(x[6]) for x in dataArray]
    # zenith = [float(x[7]) for x in dataArray]
    # dwSolar = [float(x[8]) for x in dataArray]
    # uwSolar = [float(x[9]) for x in dataArray]
    # directNormal = [float(x[10]) for x in dataArray]
    # diffuseSolar = [float(x[11]) for x in dataArray]
    # dwInfrared = [float(x[12]) for x in dataArray]
    # dwInfraredCaseTemp = [float(x[13]) for x in dataArray]
    # dwInfraredDomeTemp = [float(x[14]) for x in dataArray]
    # uwInfrared = [float(x[15]) for x in dataArray]
    # uwInfraredCaseTemp = [float(x[16]) for x in dataArray]
    # uwInfraredDomeTemp = [float(x[17]) for x in dataArray]
    # ultravioletB = [float(x[18]) for x in dataArray]
    # photosyntheticActiveRad = [float(x[19]) for x in dataArray]
    # netSolar = [float(x[20]) for x in dataArray]
    # netInfrared = [float(x[21]) for x in dataArray]
    # netRadiation = [float(x[22]) for x in dataArray]
    # airTemp = [float(x[23]) for x in dataArray]
    # relativeHumidity = [float(x[24]) for x in dataArray]
    # windSpeed = [float(x[25]) for x in dataArray]
    # windDirection = [float(x[26]) for x in dataArray]
    # pressure = [float(x[27]) for x in dataArray]

    print('## Plotting Options ##\n', *plottingOptions,
          sep=' | ', end=' |\n## Plotting Options ##')

    locationInput = input('\n Choose one data set to plot: ')

    for i in range(0, len(plottingOptions)):
        if plottingOptions[i] == locationInput:
            yAxisData = [float(x[i]) for x in dataArray]
            dataVarChosen = plottingOptions[i]

    plottingOptions = ['year', 'julianDay', 'month', 'day', 'hour', 'minute',
                       'decimalTime', 'zenith', 'dwSolar', 'uwSolar',
                       'directNormal', 'diffuseSolar', 'dwInfrared',
                       'dwInfraredCaseTemp', 'dwInfraredDomeTemp',
                       'uwInfrared', 'uwInfraredCaseTemp',
                       'uwInfraredDomeTemp', 'ultravioletB',
                       'photosyntheticActiveRad', 'netSolar', 'netInfrared',
                       'netRadiation', 'airTemp', 'relativeHumidity',
                       'windSpeed', 'windDirection', 'pressure']

    os.chdir(originalPath)

    with open('data-name-dictionary.txt', 'rb') as d:
        dataNames = pickle.loads(d.read())

    with open('station-name-dictionary.txt', 'rb') as d:
        stationNames = pickle.loads(d.read())

    # dataNameInput = "'" + dataVarChosen + "'"
    # stationNameInput = "'" + fileToRead.strip()[:3] + "'"

    dataNameInput = dataNames[dataVarChosen]
    stationNameInput = stationNames[fileToRead.strip()[:3]]

    # plotTitle = '"' + dataNameInput + ' - ' + stationNameInput + '"'
    plotTitle = dataNameInput + ' - ' + stationNameInput

    trace1 = {
        "x": decimalTime,
        # "y": dwSolar,
        "y": yAxisData,
        "mode": "lines",
        # "name": "Downwelling Solar - Penn State",
        "name": plotTitle,
        "type": "scatter"
    }
    data = Data([trace1])
    layout = {
        # "title": "Downwelling Solar for Penn State on January 1, 2017",
        "title": plotTitle,
        "xaxis": {
            "autorange": True,
            "title": "Hour of Day (UTC)",
            "type": "linear"
        },
        "yaxis": {
            "autorange": True,
            # "title": "Downwelling Solar Radiation (W/m^2)",
            "title": dataNameInput,
            "type": "linear"
        }
    }
    fig = Figure(data=data, layout=layout)
    plot_url = py.plot(fig)
