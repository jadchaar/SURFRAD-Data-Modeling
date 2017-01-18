from file_retrieval import *
from plotting import *

while True:
    try:
        getFiles = str(
            input('Retrieve data files from the SURFRAD FTP server? (y/n) '))
    except ValueError:
        print('Error: Please input a valid option (y/n)!')
        continue

    if getFiles == '':
        print('Error: Please input a valid option (y/n)!')
        continue
    elif getFiles in {'y','Y','YES','yes','Yes'}:
        break
    elif getFiles in {'n','N','NO','no','No'}:
        break
    else:
        print('Error: Please input a valid option (y/n)!')
        continue

if getFiles in {'y','Y','YES','yes','Yes'}:
    print('Initiating file retrieval program...')
    retrieve_files()
else:
    plot_graph()
