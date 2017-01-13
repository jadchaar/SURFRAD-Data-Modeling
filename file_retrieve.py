import os
import urllib
import ftplib

# urllib.urlretrieve('ftp://server/path/to/file', 'file')

# specify path other than current directory
if not os.path.exists(os.getcwd() + '/ftp_files') or os.path.exists(os.getcwd() + '/ftp'):
    createfolderYorN = input('Create a folder to store FTP files in current directory? (y/n) ')
    if createfolderYorN == 'y' or createfolderYorN == 'Y':
        print('Creating folder...')
        os.makedirs(os.getcwd() + '/ftp_files')


# path = os.getcwd()
# filename = 'L28POC_B.xpt'
#
# ftp = ftplib.FTP("Server IP")
# ftp.login("UserName", "Password")
# ftp.cwd(path)
# ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
# ftp.quit()


# link to FTP = ftp://aftp.cmdl.noaa.gov/data/radiation/surfrad/
