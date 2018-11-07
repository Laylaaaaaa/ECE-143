import shlex
import csv

features, salaries=[], []

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
        print header
        lines = [x for x in data_csv]

        for l in lines:
            features.append(l[0:9]+[l[11]])
            salaries.append(float(l[10]))
    print "done"
    return features,salaries


def salary_per_job_category():
    '''
    visualizes the average salary for each job title
    output: chart of average salary for job title
    '''

    #assert
    #features, salaries = read_data_from_excel()
    print features[0]

def salary_per_company():
    pass

def salary_per_location():
    pass

def job_titles():
    pass

def average_salary():
    pass

read_data_from_excel()
salary_per_job_category()
