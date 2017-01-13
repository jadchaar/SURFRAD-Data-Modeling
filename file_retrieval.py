import os
import ftplib


def retrieve_files():
    stationNameArray = ['Alamosa CO', 'Bondville IL', 'Boulder CO', 'Desert Rock NV',
                        'Fort Peck MT', 'Goodwin Creek MS', 'Penn State PA',
                        'Rutland VT', 'Sioux Falls SD', 'Wasco OR']

    # log into FTP
    ftp = ftplib.FTP('aftp.cmdl.noaa.gov')
    print('Logging into ftp://aftp.cmdl.noaa.gov...')
    ftp.login()
    print('FTP LOGIN SUCCESSFUL!')

    print('\n### PLOTTING PROGRAM ###\n')
    print('Step 1. Input SURFRAD Station Location')
    print('## Location Options ##\n', *stationNameArray,
          sep=' | ', end=' |\n## Location Options ##')
    # add type help for station options?
    stationName = input('\nEnter a SURFARD station: ')

    # Change String if entered as all lower case
    stationName = stationName.title()
    stationName = stationName.replace(stationName[(len(stationName) - 2):len(
        stationName)], stationName[(len(stationName) - 2):len(stationName)].upper())

    for i in range(0, len(stationName)):
        stationName = stationName.replace(' ', '_')

    ftpURL = 'data/radiation/surfrad/' + stationName + '/'
    # FTP change directory
    print('Changing FTP URL to ftp://aftp.cmdl.noaa.gov/' + ftpURL)
    ftp.cwd(ftpURL)

    print('\nStep 2. Enter Year of Data Needed')
    print('## Years ##')
    content = ftp.retrlines('NLST')

    year = input('\nEnter a year: ')
    ftpURLWithYear = year + '/'
    print('Loading...')
    ftp.cwd(ftpURLWithYear)

    print('\nStep 3. Enter Data File(s) to Retrieve')
    print('## Data Files (location acronym | two digits of year | julian day) ##')
    content = ftp.retrlines('NLST')

    downloadAllResponse = input(
        '\nDownload all files in this directory or only a single one? (all/single) ')

    if downloadAllResponse == 'all' or downloadAllResponse == 'ALL':
        # change default directory of FTP storage
        if not os.path.exists(os.getcwd() + '/ftp_files'):
            createfolderYorN = input(
                'Create a folder to store FTP files in current directory? (y/n) ')
            if createfolderYorN == 'y' or createfolderYorN == 'Y':
                print('Creating folder...')
                os.makedirs(os.getcwd() + '/ftp_files')

        original_directory = os.getcwd()
        os.chdir(os.getcwd() + '/ftp_files')

        print('\nTransferring files to ' + os.getcwd())
        filenames = ftp.nlst()
        for filename in filenames:
            # ftp.retrbinary('RETR ' + filename, open(filename, 'wb').write)
            file = open(filename, 'wb')
            ftp.retrbinary('RETR ' + filename, file.write)
            file.close()
        print('File transfer complete!')
    elif downloadAllResponse == 'single' or downloadAllResponse == 'SINGLE':
        filename = input('\nEnter a data file to read: ')

        if filename[(len(filename) - 4):len(filename)] != '.dat':
            filename += '.dat'

        # change default directory of FTP storage
        if not os.path.exists(os.getcwd() + '/ftp_files'):
            createfolderYorN = input(
                'Create a folder to store FTP files in current directory? (y/n) ')
            if createfolderYorN == 'y' or createfolderYorN == 'Y':
                print('Creating folder...')
                os.makedirs(os.getcwd() + '/ftp_files')

        original_directory = os.getcwd()
        os.chdir(os.getcwd() + '/ftp_files')

        print('\nTransferring ' + filename + ' to ' + os.getcwd())
        # ftp.retrbinary('RETR ' + filename, open(filename, 'wb').write)
        file = open(filename, 'wb')
        ftp.retrbinary('RETR ' + filename, file.write)
        print('File transfer complete!')
        file.close()

    ftp.quit()

    os.chdir(original_directory)
