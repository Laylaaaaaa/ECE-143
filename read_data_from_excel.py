import numpy as np
import shlex
import csv

def read_data_from_excel(file_path='/Users/shawnwinston/Desktop/ece_143/Train_rev1_salaries.csv'):
    '''
    reads raw data from an execl file and stores it in a dxn list
    where n is the number of data examples and d is the number
    of categories

    input: file name of where to read data from

    output:nxd list of extracted raw data

    '''

    assert isinstance(file_path, str)

    print "Reading data..."

    with open(file_path) as data:
        data_csv = csv.reader(data)

        header = data.readline()
        lines = [x for x in data_csv]

        features, salaries=[], []
        for l in lines:
            features.append(l[0:9]+[l[11]])
            salaries.append(float(l[10]))
    print "done"

read_data_from_excel()