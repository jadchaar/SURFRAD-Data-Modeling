from file_retrieval import retrieve_files
from generate_dictionary import form_dict
import os.path
from plotting import plot_graph
import sys

print('Checking for and generating required dependencies if necessary...\n')
for i in {'data-name-dictionary.txt', 'station-name-dictionary.txt', 'station-abbreviation-dictionary.txt'}:
    if not(os.path.isfile(i)):
        form_dict()
        break

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

# Ask if the user wants to enter the plotting program again
while True:
    try:
        anotherPlot = str(
            input('Generate another plot? (y/n) '))
    except ValueError:
        print('Error: Please input a valid option (y/n)!')
        continue

    if anotherPlot == '':
        print('Error: Please input a valid option (y/n)!')
        continue
    elif anotherPlot in {'y','Y','YES','yes','Yes'}:
        break
    elif anotherPlot in {'n','N','NO','no','No'}:
        break
    else:
        print('Error: Please input a valid option (y/n)!')
        continue

if anotherPlot in {'y','Y','YES','yes','Yes'}:
    print('Initiating plotting program...')
    plot_graph()
else:
    print('Exiting program...')
    sys.exit(0)

p.terminate()
