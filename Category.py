import csv
import matplotlib.pyplot as plt

def Read_data_Generate_JobCategory():
    '''Read job category and location data of Top 20 locations and job category and company data of Top 20 companys from file "Train_rev1.csv".
        Count the number of job categories of each location and company.
        Find the most common job category of each location and company.
        Plot bar chart for job category vs company and job category vs company.'''
    file_name = 'Train_rev1.csv'
    # Top 20 locations
    location_dict = {'UK': dict(), 'London': dict(), 'South East London': dict(), 'The City': dict(),
                     'Manchester': dict(), 'Leeds': dict(), 'Birmingham': dict(), 'Central London': dict(),
                     'West Midlands': dict(), 'Surrey': dict(), 'Reading': dict(), 'Bristol': dict(),
                     'Nottingham': dict(), 'Sheffield': dict(), 'Aberdeen': dict(), 'Hampshire': dict(),
                     'Belfast': dict(), 'East Sheen': dict(), 'Milton Keynes': dict(), 'Berkshire': dict()}
    # Top 20 companies
    company_dict = {'UKStaffsearch': dict(), 'CVbrowser': dict(), 'London4Jobs': dict(), 'Hays': dict(),
                    'JAM Recruitment Ltd': dict(), 'Office Angels': dict(), 'Jobsite Jobs': dict(),
                    'Perfect Placement': dict(), 'ARRAY': dict(), 'JOBG8': dict(), 'Matchtech Group plc.': dict(),
                    'Penguin Recruitment': dict(), 'Randstad': dict(), 'Adecco': dict(),
                    'Michael Page Finance': dict(), 'Adecco Group': dict(), 'BMS Sales Specialists LLP': dict(),
                    'COREcruitment International': dict(), 'Page Personnel Finance': dict()}

    # Open file, read data and store in dict
    # Count the number of job categories of each location and company.
    with open(file_name,encoding="ISO-8859-1") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for data in csv_reader:
            if data[0] == '':
                break
            if data[4] in location_dict.keys():
                if data[8] in location_dict[data[4]].keys():
                    location_dict[data[4]][data[8]] += 1
                else:
                    location_dict[data[4]][data[8]] = 1
            if data[7] in company_dict.keys():
                if data[8] in company_dict[data[7]].keys():
                    company_dict[data[7]][data[8]] += 1
                else:
                    company_dict[data[7]][data[8]] = 1
    csv_file.close()

    # store the number of job categories of each location and company in file
    # Find the most common job category of each location and company and store them in file
    f = open('result.txt','w')
    f1 = open('MaxCategoryForLocation.txt', 'w')
    f2 = open('MaxCategoryForCompany.txt', 'w')
    f.write('Loction' + '\n')
    for key in location_dict:
        f.writelines(key + ' ' + str(len(location_dict[key])) + '\n')
        max_num = 0
        for C_key in location_dict[key]:
            if location_dict[key][C_key] > max_num:
                max_num = location_dict[key][C_key]
                max_cat = C_key
        f1.writelines(key+ "-"+ '"' +max_cat + '"' + "-" + str(max_num) + '\n')
    f.write('\n'*3)
    f.write('Company' + '\n')
    for key in company_dict:
        f.writelines(key + ' ' + str(len(company_dict[key])) + '\n')
        max_num = 0
        for C_key in company_dict[key]:
            if company_dict[key][C_key] > max_num:
                max_num = company_dict[key][C_key]
                max_cat = C_key
        f2.writelines(key + "-" + max_cat + "-" + str(max_num) + '\n')
    f.close()
    f1.close()
    f2.close()


    # figure: job category_vs location
    location_list = sorted(location_dict.items(), key = lambda item : len(item[1]), reverse=True)
    indexes = range(len(location_dict))
    labels = list()
    values = list()
    font1 = {'family': 'Times New Roman',
             'weight': 'normal',
             'size': 20,
             }
    font2 = {'family': 'Times New Roman',
             'weight': 'normal',
             'size': 25,}
    for key in location_list:
        labels.append(key[0])
        values.append(len(key[1]))
    width = 0.7
    my_colors = ['lightskyblue', 'yellowgreen']
    plt.figure(figsize=(15, 10))
    fig = plt.barh(labels, values, width, color=my_colors)
    plt.ylabel("Location",font1)
    plt.xlabel("The number of Job Category",font1)
    plt.title("The number of job category of location",font2)
    plt.show()

    # figure: job category vs company
    company_list = sorted(company_dict.items(), key=lambda item: len(item[1]), reverse=True)
    indexes = range(len(company_dict))
    labels = list()
    values = list()
    for key in company_list:
        labels.append(key[0])
        values.append(len(key[1]))
    width = 0.7
    my_colors = ['lightskyblue', 'yellowgreen']
    plt.figure(figsize=(15, 10))
    fig = plt.barh(labels, values, width, color=my_colors)
    plt.ylabel("Company",font1)
    plt.xlabel("The number of Job Category",font1)
    plt.title("The number of job category of company",font2)
    plt.show()
