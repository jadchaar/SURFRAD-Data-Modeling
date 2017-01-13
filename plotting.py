# import numpy as np
import matplotlib.pyplot as plt

# plotly configuration
import plotly
plotly.tools.set_credentials_file(
    username='jadchaar', api_key='vRIzy7SgLxPJOzEYQzvM')
plotly.tools.set_config_file(world_readable=True,
                             sharing='public')
import plotly.plotly as py
from plotly.graph_objs import *

with open('psu17001.dat', 'r') as f:
    stationName = f.readline().strip()
    secondLine = f.readline().strip()
    dataArray = []
    # next(f)
    # next(f)
    for line in f:
        dataArray.append([float(x) for x in line.split()])
    f.close()

# Extract data from second line
latitude, longitude, elevation = secondLine.split("  ")[:3]
elevation = elevation.replace(" m version 1", "")
latitude = float(latitude)
longitude = float(longitude)
elevation = int(elevation)


yearCol = [int(x[0]) for x in dataArray]
julianDayCol = [int(x[1]) for x in dataArray]
monthCol = [int(x[2]) for x in dataArray]
dayCol = [int(x[3]) for x in dataArray]
hourCol = [int(x[4]) for x in dataArray]
minuteCol = [int(x[5]) for x in dataArray]
decimalTimeCol = [float(x[6]) for x in dataArray]
zenithCol = [float(x[7]) for x in dataArray]
dwSolarCol = [float(x[8]) for x in dataArray]
uwSolarCol = [float(x[9]) for x in dataArray]
directNormalCol = [float(x[10]) for x in dataArray]
diffuseSolarCol = [float(x[11]) for x in dataArray]
dwInfraredCol = [float(x[12]) for x in dataArray]

# print('Station:', stationName, ' | ', 'Latitude:', latitude, ' | ',
#       'Longitude:', longitude, ' | ', 'Elevation:', elevation)

plotTitle = 'Downwelling Solar (Lat: ' + \
    str(latitude) + ' Lon: ' + str(longitude) + ')'

# Plot Downwelling Solar Radiation in matplotlib
# Check against this: https://www.esrl.noaa.gov/gmd/grad/surfrad/dataplot.html
# plt.plot(decimalTimeCol, dwSolarCol)
# plt.title(plotTitle)
# plt.xlim(0, 24)
# plt.ylabel('Downwelling Solar')
# plt.xlabel('Hour of Day (UTC)')
# plt.show()

# In [1]:
trace1 = {
    "x": decimalTimeCol,
    "y": dwSolarCol,
    "mode": "lines",
    "name": "Downwelling Solar - Penn State",
    "type": "scatter"
}
data = Data([trace1])
layout = {
    "title": "Downwelling Solar Radiation for Penn State, PA on January 1, 2017",
    "xaxis": {
        "autorange": True,
        "title": "Hour of Day (UTC)",
        "type": "linear"
    },
    "yaxis": {
        "autorange": True,
        "title": "Downwelling Solar Radiation (W/m^2)",
        "type": "linear"
    }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
