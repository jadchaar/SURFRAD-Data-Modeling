from file_retrieval import retrieve_files
from generate_dictionary import form_dict
import os
from plotting import plot_graph
import sys

print('Checking for and generating required dependencies if necessary...\n')

fileContents = os.listdir(os.getcwd())
fileContents = set(fileContents)

checkNames = {'data-name-dictionary.json', 'station-name-dictionary.json', 'station-abbreviation-dictionary.json'}
if fileContents.isdisjoint(checkNames):
    form_dict()
else:
    while True:
        try:
            jsonOverride = str(input('Previously generated dictionaries found. Override? (y/n) '))
        except ValueError:
            print('Error: Please input a valid option (y/n)!')
            continue

        if jsonOverride == '':
            print('Error: Please input a valid option (y/n)!')
            continue
        elif jsonOverride in {'y', 'Y', 'YES', 'yes', 'Yes'}:
            form_dict()
            break
        elif jsonOverride in {'n', 'N', 'NO', 'no', 'No'}:
            break
        else:
            print('Error: Please input a valid option (y/n)!')
            continue

while True:
    try:
        getFiles = str(
            input('\nRetrieve data files from the SURFRAD FTP server? (y/n) '))
    except ValueError:
        print('Error: Please input a valid option (y/n)!')
        continue

    if getFiles == '':
        print('Error: Please input a valid option (y/n)!')
        continue
    elif getFiles in {'y', 'Y', 'YES', 'yes', 'Yes'}:
        break
    elif getFiles in {'n', 'N', 'NO', 'no', 'No'}:
        break
    else:
        print('Error: Please input a valid option (y/n)!')
        continue

if getFiles in {'y', 'Y', 'YES', 'yes', 'Yes'}:
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
    elif anotherPlot in {'y', 'Y', 'YES', 'yes', 'Yes'}:
        break
    elif anotherPlot in {'n', 'N', 'NO', 'no', 'No'}:
        break
    else:
        print('Error: Please input a valid option (y/n)!')
        continue

if anotherPlot in {'y', 'Y', 'YES', 'yes', 'Yes'}:
    print('Initiating plotting program...')
    plot_graph()
else:
    print('Exiting program...')
    sys.exit(0)

p.terminate()
