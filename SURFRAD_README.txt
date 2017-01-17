DESCRIPTION OF SURFRAD DAILY DATA FILES

Updated on Jan. 14, 2013 to clarify terms and change FTP addresses

Updated on June 10, 2005 to include information about correcting reported
UVB data in SURFRAD data files (which assume a total ozone value of 300 Dobson
Units) to the actual total ozone.

Updated on March 31, 2004 to explain: 1) improvements to the net solar
calculation, 2) increased accuracy of historical SURFRAD UVB data, and 3) a
correction that has been applied to all diffuse solar measurements prior to the
2001 instrument exchanges.  In 2001 Eppley 8-48 pyranometers replaced
conventional thermopile pyranometers as the diffuse instrument in the SURFRAD
suite.

Updated on July 5, 2002 to explain details of the net solar calculation

Updated April 13, 1999 -- The UVB processing has been improved to compute
UVB erythemal-weighted irradiance.  Also, calibration factors derived annually
from standard instruments at NOAA's Central UV Calibration Facility are applied
to the network UVB instruments.  This improvement has been applied to all data
from the beginning of the data record for each station.  The method used is
described in the UVB section below.  Before this, a representative factory
calibration corresponding to a representative solar zenith angle (40 degrees)
was applied to all data, regardless of the solar zenith angle that the
measurement was made.


FILENAME INFORMATION:

SURFRAD data files contain one day of data for one station.  The FTP directories
from which SURFRAD data are distributed are organized by station and year.  The
naming convention for SURFRAD data filenames is "stayyjjj.dat", where sta is a
three-letter station identifier, yy represents the last two digits of the year
(i.e., 95 for 1995, 00 for 2000), and jjj is the day of year. A "day of year"
in a filename that is less than 100 would be preceded by one or two zeros,
e.g., day 75 would appear as 075, day 2 would appear as 002 in the filename. The
SURFRAD processing software is year 2000 compliant.  The year within the data
files is written unambiguously with 4 digits on each line.

"bon" is the station identifier for Bondville, Illinois
"fpk" is the station identifier for Fort Peck, Montana
"gwn" is the station identifier for Goodwin Creek, Mississippi
"tbl" is the station identifier for Table Mountain, Colorado
"dra" is the station identifier for Desert Rock, Nevada
"psu" is the station identifier for Penn State, Pennsylvania
"sxf" is the station identifier for Sioux Falls, South Dakota

The extension ".dat" is used because both radiation and meteorological data
are included.  The file "bon95099.dat" contains all of the radiation and
meteorological data for Bondville on day 99 of 1995.


Daily SURFRAD data files for each station may be downloaded from the following
location:

ftp://aftp.cmdl.noaa.gov/data/radiation/surfrad/

To get to a specific file, advance to the appropriate station directory, and
then to the specific year directory, e.g., ftp://aftp.cmdl.noaa.gov/data/radiation/surfrad/Bondville_IL/2003/for Bondville, 2003 data


DATA STRUCTURE:

SURFRAD data are organized into daily files of one- or three-minute data, and
are written in ASCII text. Before 1-jan. 2009 the data were reported as 3-min averages;On and after 1-Jan. 2009 the SURFRAD data are reported as 1-min. averages.SURFRAD data may be read with the section of FORTRAN code listed
below. The format was specified in such a way to ensure that all entries are
separated by at least one space so that the files may be read with free format.
SURFRAD follows the quality control (QC) philosophy of the BSRN. Bad data are deleted, but questionable data are only flagged. Integer QC flags follow each data point.

A QC flag of zero indicates that the corresponding data point is good, having
passed all QC checks.  A value greater than 0 indicates that the data failed one
level of QC.  For example, a QC value of 1 means that the recorded value is
beyond a physically possible range, or it has been affected adversely in some manner to produce a knowingly bad value.  A value of 2 indicates that the data value failed the second level QC check, indicating that the data value may be
physically possible but should be used with scrutiny, and so on.  Missing
values are indicated by -9999.9 and should always have a QC flag of 1.


The following section of FORTRAN code may be used to read daily SURFRAD files:

	parameter (nlines=1440)
	character*80	station_name
c
	integer	year,month,day,jday,elevation,version
	integer	min(nlines),hour(nlines)
c
	real	latitude,longitude,dt(nlines),zen(nlines),direct_n(nlines)
	real	dw_solar(nlines),uw_solar(nlines)
	real	diffuse(nlines),dw_ir(nlines),dw_casetemp(nlines)
	real	dw_dometemp(nlines),uw_ir(nlines),uw_casetemp(nlines)
	real	uw_dometemp(nlines),uvb(nlines),par(nlines)
	real	netsolar(nlines),netir(nlines),totalnet(nlines),temp(nlines)
	real	rh(nlines),windspd(nlines),winddir(nlines),pressure(nlines)
c
	integer	qc_direct_n(nlines),qc_netsolar(nlines),qc_netir(nlines)
	integer	qc_dwsolar(nlines),qc_uwsolar(nlines),qc_diffuse(nlines)
	integer	qc_dwir(nlines),qc_dwcasetemp(nlines)
	integer	qc_dwdometemp(nlines),qc_uwir(nlines)
	integer	qc_uwcasetemp(nlines),qc_uwdometemp(nlines)
	integer	qc_uvb(nlines),qc_par(nlines)
	integer	qc_totalnet(nlines),qc_temp(nlines)
	integer	qc_rh(nlines),qc_windspd(nlines),qc_winddir(nlines)
	integer	qc_pressure(nlines)
c
c
        lun_in = 20
        open(unit=lun_in,file=[filename.dat],status='old',readonly)
.
.
.
	read (lun_in,10) station_name
  10	format(1x,a)
	read(lun_in,*) latitude, longitude, elevation
c
	icount = 0
	do i = 1,nlines
c
	read(lun_in,30,end=40) year,jday,month,day,hour(i),min(i),dt(i),
     1	zen(i),dw_solar(i),qc_dwsolar(i),uw_solar(i),qc_uwsolar(i),direct_n(i),
     2	qc_direct_n(i),diffuse(i),qc_diffuse(i),dw_ir(i),
     3	qc_dwir(i),dw_casetemp(i),qc_dwcasetemp(i),dw_dometemp(i),
     4	qc_dwdometemp(i),uw_ir(i),qc_uwir(i),uw_casetemp(i),
     5	qc_uwcasetemp(i),uw_dometemp(i),qc_uwdometemp(i),uvb(i),
     6	qc_uvb(i),par(i),qc_par(i),netsolar(i),qc_netsolar(i),netir(i),
     7	qc_netir(i),totalnet(i),qc_totalnet(i),temp(i),qc_temp(i),rh(i),
     8	qc_rh(i),windspd(i),qc_windspd(i),winddir(i),qc_winddir(i),
     9	pressure(i),qc_pressure(i)
c
	icount = icount + 1
  30	format(1x,i4,1x,i3,4(1x,i2),1x,f6.3,1x,f6.2,20(1x,f7.1,1x,i1))
c
	enddo
  40	type *,'end of file reached, ',icount,' records read'
.
.
.

The file structure includes two header records; the first has the name of the
station, and the second gives the station's latitude, longitude, elevation above
mean sea level in meters, and the version number of the file.  These are
followed by at most, 1440 lines of 1-min. data or 480 lines of 3-min. data.
Files are organized in Universal Coordinated Time (UTC).  The date and time
are given on every line.  Data are reported as 1- or 3-minute averages of one-second samples.  Reported times are the end times of the 1- or 3-min. averaging periods, i.e., the data given for 0000 UTC are averaged over the period from 2359 (or 2357) of the previous UTC day, to 0000 UTC. The solar zenith angle is reported in degrees on each line of data. It is computed for the central time of the averaging period of the sampled data. Missing-data periods within the files are not filled in with missing values, therefore, a file with missing periods will have fewer than 1440 lines for 1-min. data, or 480 lines for 3-min. data.

Radiation values are reported to the tenths place.  Although this is beyond
the accuracy of the instruments, data are reported in this manner in order to
maintain the capability of backing out the raw voltages at the accuracy that
they were originally reported.

The variables, their data type, and description are given below:

station_name	character	station name, e. g., Goodwin Creek
latitude		real	latitude in decimal degrees (e. g., 40.80)
longitude		real	longitude in decimal degrees (e. g., 105.12)
elevation		integer	elevation above sea level in meters
year			integer	year, i.e., 1995
jday			integer	Julian day (1 through 365 [or 366])
month			integer	number of the month (1-12)
day			integer	day of the month(1-31)
hour			integer	hour of the day (0-23)
min			integer	minute of the hour (0-59)
dt			real	decimal time (hour.decimalminutes, e.g., 23.5 = 2330)
zen			real	solar zenith angle (degrees)
dw_solar		real	downwelling global solar (Watts m^-2)
uw_solar		real	upwelling global solar (Watts m^-2)
direct_n		real	direct-normal solar (Watts m^-2)
diffuse		real	downwelling diffuse solar (Watts m^-2)
dw_ir			real	downwelling thermal infrared (Watts m^-2)
dw_casetemp		real	downwelling IR case temp. (K)
dw_dometemp		real	downwelling IR dome temp. (K)
uw_ir			real	upwelling thermal infrared (Watts m^-2)
uw_casetemp		real	upwelling IR case temp. (K)
uw_dometemp		real	upwelling IR dome temp. (K)
uvb			real	global UVB (milliWatts m^-2)
par			real	photosynthetically active radiation (Watts m^-2)
netsolar		real	net solar (dw_solar - uw_solar) (Watts m^-2)
netir			real	net infrared (dw_ir - uw_ir) (Watts m^-2)
totalnet		real	net radiation (netsolar+netir) (Watts m^-2)
temp			real	10-meter air temperature (?C)
rh			real	relative humidity (%)
windspd		real	wind speed (ms^-1)
winddir		real	wind direction (degrees, clockwise from north)
pressure		real	station pressure (mb)


Diffuse solar and station pressure were not originally part of the SURFRAD
suite of measurements.  These were added to all stations in the 1996-97
time frame.  Early data files from all stations have places for these
parameters, but they are filled with missing values until the time when those
instruments were installed.


Diffuse and global solar processing:

It is not unusual that thermopile-based solar instruments register a small
negative signal at night. Most of this error is attributed to the thermopile
cooling to space.  These erroneous offsets are manifested in the global and
diffuse solar measurements, but not in the pyrheliometer that measures direct-normal solar irradiance. Erroneous nighttime offsets in the diffuse and global solar measurements of between 0 and -10 Wm^-2 are typical, but can be as great as 30 Wm^-2.  Because this behavior is common, only nighttime signals that drop below -30 are flagged. The erroneous offset is also present in daytime data, but is masked by the solar signal.  A way to correct this error in the daytime diffuse measurements has been developed.  It is described in Dutton et al, 2001 (J. Atmos. and Ocean Tech., 18, 297-314). Their method involves the development of a relationship between the thermopile output of a collocated pyrgeometer and the negative diffuse signals for nighttime periods. That relationship is then
applied to all diffuse data (night and day).

As of March 19, 2004, all diffuse solar data prior to the 2001 instrument
exchanges at each station have been corrected using the Dutton et al. method.

The Eppley model 8-48 pyranometer, which has been used for the diffuse
measurement since the 2001 instrument exchanges, does not have this problem.
The model 8-48 pyranometer relies on a differential signal between a black and a
white surface on the detector.  Since these two surfaces emit the same in the
infrared, the differential signal owing to infrared cooling of the sensor's
surface is zero.  Thus there is little or no erroneous offset owing to radiative
cooling of the 8-48 sensor at night (or in the day).

The global solar sensor has the same infrared cooling problem, but solar heating
inside of the dome during the day prevents development of a simple relationship
using nighttime data that is applicable during the day.  Solar heating is not a
problem with the diffuse pyranometer because it is, by practice, shaded.
Therefore, the global solar measurement is not yet correctable, and should only
be used in cases when the direct-normal and diffuse solar measurements are not  available.


Net radiation processing:

Net radiation, net solar, net infrared, and total net (net solar + net infrared)
are computed and reported in the daily processed files.  In computing net solar
(downwelling solar - upwelling solar) the best measure of downwelling solar is
used.  When direct-normal and diffuse solar are available, and deemed to be of good quality, their sum (direct-normal*cosSZA + diffuse) is used for the downwelling solar in the net solar calculation. Otherwise, the global solar measurement is used.  Whenever any of the solar measurements are negative (owing to cooling of the thermopile near dusk and dawn), they are set to 0 before computing the net radiation.

Net solar is computed for solar zenith angles between 0 and 96 degrees.  The
net solar calculation is extended beyond 90, to 96 degrees to account for civil
twilight.

All radiation parameters, except UVB, are reported in units of Watts m^-2;
UVB is reported in milliWatts m^-2.


UVB processing:

The UVB flux is given as the total measured surface UVB flux convoluted
with the erythemal action spectrum, i.e., that part of the UVB spectrum
responsible for sun burns on human skin (erythema) and DNA damage.  It is
reported in this way because the response function of the UVB instrument
approximates the erythemal action spectrum; thus the reported value is most
representative of what the instrument is actually measuring.

The erythemal UVB irradiance reported in SURFRAD data files is computed for
300 Dobson units of ozone.  This is done because the ozone value over the
stations is unknown during the near real-time processing.  If the ozone
for a particular day is less than 300 Dobson units, then the reported UVB
irradiance would be less than it should be. If the user would like to correct reported SURFRAD UVB measurements for the actual ozone, correction tables are available. Contact the webmaster for these tables.

The field UVB instruments are calibrated against a triad of "standard" UVB
instruments that are maintained by NOAA's Central UV Calibration Facility.  The
standard instruments are periodically calibrated in the sun by comparing
their broadband measurements to the integrated output of UV spectroradiometers.
These calibrations are transferred to the field instruments just before
they are deployed in the network by operating them side-by-side for a
few days.  To accomplish this transfer, a scale factor, which is simply a ratio
of the test instrument's daily integral to that of the mean of the standards, is
computed for each day that the test UVB instrument is run alongside the
standards.  The mean of the daily scale factors is used to transfer the standards' well maintained calibrations to the test instruments when they are deployed in the field.

Mean calibration factors for the UVB standards are computed as a function of solar zenith angle, and are applied to the field instrument as such in the daily
processing.  For example, to compute the UVB irradiance, the output voltage,
is multiplied times the Standards' calibration factor for the solar
zenith angle that the measurement was made, then that result is divided by
the scale factor for that field instrument.

The following table lists the UVB Standards' calibration information computed
using the September 23, 1997 UV Spectroradiometer intercomparison data.

erythemal    solar
conversion   zenith
factor       angle
(W m^-2 / V)

0.136        0.0 extrapolated
0.136        5.0
0.136        10.0
0.135        15.0
0.134        20.0
0.133        25.0
0.132        30.0
0.131        35.0
0.130        40.0
0.129        45.0
0.128        50.0
0.128        55.0
0.129        60.0
0.132        65.0
0.138        70.0
0.147        75.0
0.164        80.0
0.191        85.0
0.220        90.0 extrapolated


Similar calibration tables for the three UVB standards were computed for June 22, 2003, they are:

erythemal    solar
conversion   zenith
factor       angle
(W m^-2 / V)

0.150	        0.0   extrapolated
0.150        5.0
0.150       10.0
0.149       15.0
0.148       20.0
0.147       25.0
0.145       30.0
0.144       35.0
0.143       40.0
0.141       45.0
0.140       50.0
0.140       55.0
0.141       60.0
0.144       65.0
0.149       70.0
0.159       75.0
0.177       80.0
0.206       85.0
0.240       90.0 extrapolated


There is evidence that the standards calibration changed linearly
between these benchmark years.  Therefore, code that applies them in the SURFRAD
processing algorithm has been written to linearly interpolate the standards
calibration to the day being processed.  As of 2 Sept. 2004, all SURFRAD data
has been reprocessed to include these improved UVB calibrations.


PAR processing:

To be consistent with other reported radiometric data in the file, values of
photosynthetically active radiation (PAR) are reported in units of Wm^-2.  The
factory calibration for our Quantum sensors that measure PAR does not transform
raw output from the instrument to these units; rather, it converts the sensor
output to umoles (of photons) m^-2 s^-1.  These units are converted to Wm^-2 by
dividing umoles m^-2 s^-1 by 4.6, which is the conversion factor derived for the
solar spectrum.  To convert the reported value back to the original units,
simply multiply our reported values times 4.6.  The theoretical basis for
converting umoles (of photons) m^-2 s^-1 to Wm^-2 for various light sources
(including the sun) is described in Proceedings of the NATO Advanced Study
Institute on Advanced Agricultural Instrumentation, 1984. W. G. Gensler (ed.),
Martinus Nijnoff Publishers, Dordrect, The Netherlands.

QUALITY CONTROL AND QUALITY ASSURANCE

SURFRAD data distributed on the ftp site are provisional.  NOAA has attempted to
produce the best data set possible, however the data quality is constrained by
measurement accuracies of the instruments and the quality of the calibrations.
Regardless, NOAA attempts to ensure the best quality possible through quality
assurance and quality control.  The data are subjected to automatic procedures
as the daily files are processed.  At present, they are subjected only to this
first-level check, and a daily "eye" check before being released, however, as
quality control procedures become more refined, they will be applied, and new
versions of the data files will be generated.

Quality assurance methods are in place to ensure against premature
equipment failure in the field and post deployment data problems.  For
example, all instruments at each station are exchanged for newly calibrated
instruments on an annual basis.  Calibrations are performed by world-
recognized organizations.  Pyranometers and pyrheliometers have been calibrated
at the National Renewable Energy Laboratory (NREL) in Golden, Colorado, or the World Meteorological Organization's (WMO) Region 4 Regional Solar Calibration Center at NOAA in Boulder, Colo.

SURFRAD pyrgeometers are calibrated using three standards maintained at
NOAA's Field Test and Calibration Facility at Table Mountain near Boulder,
CO. SURFRAD pyrometer standards' calibrations are traceable to the WISG world standard device in Davos, Switzerland, where they are calibrated annually.  In general, all of the standards at NOAA/Boulder and at DOE/NREL are traceable to world standards or an equivalent.  Calibration factors for the UVB instrument are transferred from three standards maintained by NOAA's National UV Calibration Facility in Boulder.  Finally, in order to maintain continuity between the returned instruments and their replacements, all instruments are gauged against three standard instruments before and after field deployment.


INSTRUMENTS:

1.	The Yankee UVB Broadband Radiometer

The UVB radiometer measures erythemally weighted UVB irradiance in the range
from 280 to 320 nm.  Field UVB instruments are calibrated by referencing them to
three standard instruments that are rigorously maintained by NOAA's Central UV
Calibration Facility. Calibrations for these instruments are applied as a
function of solar zenith angle.

2.	The LI-COR Quantum (PAR) Sensor

The LI-COR Quantum (Photosynthetically Active Radiation, or PAR) sensor
measures radiation in the band from 400 to 700 nm, which is the part of the
solar spectrum that activates photosynthesis in plants.  The PAR sensor sits
on the main platform at SURFRAD stations and collects downwelling global
radiation in the PAR band.  These instruments are sent to the manufacturer
annually for calibration.

3.	The Normal Incidence Pryheliometer (NIP)

The NIP measures direct-normal solar radiation in the broadband spectral range from 280 to 3000 nm.  Those used at SURFRAD stations are calibrated nominally
on a yearly basis at the National Renewable Energy Laboratory (NREL) in
Golden, Colorado.

4.	The Spectrolab SR-75 pyranometer

Pyranometers measure global downwelling and upwelling solar irradiance at
SURFRAD stations.  These instruments are sensitive to the same broadband
spectral range as the NIP, 280 to 3000 nm.  They are calibrated
on a yearly basis.

An inherent problem with solid black thermopile pyrometers, such as the SR-75 and Eppley PSP, is that their sensor cools to space (if it is directed upward) and that causes a negative signal.  This is apparent at night where it shows up as an erroneous negative irradiance that can be as great as -30 Wm^-2.


5.	Eppley 8-48 "black and white" pyranometer

This pyranometer has been used for the diffuse solar measurement since 2001. The 8-48 has been found to have desirable properties for this measurement because it does not use a solid black surface for the detector and thus does not have the "nighttime" offset problem.  These instruments are sensitive to the same broadband spectral range as the NIP and solar, 280 to 3000 nm.  They are also calibrated on a yearly basis.

6.	Precision Infrared Radiometer (PIR)

Two PIRs measure upwelling and downwelling thermal infrared irradiance.
They are sensitive to the spectral range from 3000 to 50,000 nm.  NOAA maintains
three standard PIRs that are calibrated annually by a world-reputable
organization.  These standards are used to calibrate field PIRs.
