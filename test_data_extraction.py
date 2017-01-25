# Note about .dat files
# 48 data values on one line including 0 seperators between data columns
# 28 actual data points

with open('psu17001.dat', 'r') as f:
    stationName = f.readline().strip()
    secondLine = f.readline().strip()
    dataArray = []
    # next(f)
    # next(f)
    for line in f:
        dataArray.append([float(x) for x in line.split()])
    f.close()

print(dataArray[3])

for i in range(0, len(dataArray)):
    del dataArray[i][9:48:2]

print(dataArray[3])

# year = [int(x[0]) for x in dataArray]
# julianDay = [int(x[1]) for x in dataArray]
# month = [int(x[2]) for x in dataArray]
# day = [int(x[3]) for x in dataArray]
# hour = [int(x[4]) for x in dataArray]
# minute = [int(x[5]) for x in dataArray]
# decimalTime = [float(x[6]) for x in dataArray]
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
