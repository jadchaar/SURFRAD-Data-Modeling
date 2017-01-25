#!~/anaconda/envs/plotting/bin/python
import configparser
import os
# import pickle
import json
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
        for line in f:
            dataArray.append([float(x) for x in line.split()])
        f.close()

    # Remove 0 seperators from dat files
    for i in range(0, len(dataArray)):
        del dataArray[i][9:48:2]

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

    decimalTime = [float(x[6]) for x in dataArray]

    print('## Plotting Options ##\n', *plottingOptions,
          sep=' | ', end=' |\n## Plotting Options ##')

    locationInput = input('\n Choose one data set to plot: ')

    for i in range(0, len(plottingOptions)):
        if plottingOptions[i] == locationInput:
            if i in {0, 1, 2, 3, 4, 5}:
                yAxisData = [int(x[i]) for x in dataArray]
                dataVarChosen = plottingOptions[i]
            else:
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

    # with open('data-name-dictionary.txt', 'rb') as d:
    #     dataNames = pickle.loads(d.read())
    #
    # with open('station-name-dictionary.txt', 'rb') as d:
    #     stationNames = pickle.loads(d.read())

    with open('data-name-dictionary.json', 'r') as d:
        dataNames = json.load(d)

    with open('station-name-dictionary.json', 'r') as d:
        stationNames = json.load(d)

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
