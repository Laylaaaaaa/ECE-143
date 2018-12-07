import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sly_ctg= pd.read_csv('Train_rev1.csv',usecols=[8,10])
sly_cpn= pd.read_csv('Train_rev1.csv',usecols=[7,10])
sly_lct= pd.read_csv('Train_rev1.csv',usecols=[4,10])

slr=list(sly_ctg.SalaryNormalized)

ctg=list(sly_ctg.Category)
cpn=list(sly_cpn.Company)
lct=list(sly_lct.LocationNormalized)

list_ctg=list(zip(ctg,slr))
list_cpn=list(zip(cpn,slr))
list_lct=list(zip(lct,slr))

ctg1=cpn1=lct1=[]
ctg_slr1=ctg_slr2=[]
cpn_slr1=cpn_slr2=[]
lct_slr1=lct_slr2=[]

for j in {'IT Jobs','Engineering Jobs','Accounting & Finance Jobs','Healthcare & Nursing Jobs','Sales Jobs','Other/General Jobs','Teaching Jobs','Hospitality & Catering Jobs','PR, Advertising & Marketing Jobs','Trade & Construction Jobs','HR & Recruitment Jobs','Admin Jobs','Retail Jobs','Customer Services Jobs','Legal Jobs','Manufacturing Jobs','Logistics & Warehouse Jobs','Social work Jobs','Consultancy Jobs','Travel Jobs'}:
	count=salary=av_slr=0
	for i in list_ctg:
		if i[0] == j:
			count+=1
			salary+=i[1]
	av_slr=int(salary/count)
	ctg1.append(j)
	ctg_slr1.append(av_slr)

ctg_dict1=dict(zip(ctg1,ctg_slr1))
ctg_dict2=dict(sorted(ctg_dict1.items(), key = lambda x:x[1],reverse = False))
ctg2=list(ctg_dict2.keys())
ctg_slr2=list(ctg_dict2.values())
print(ctg_dict2)
print(ctg2)
print(ctg_slr2)

for j in {'UKStaffsearch','CVbrowser','London4Jobs','Hays','JAM Recruitment Ltd','Office Angels','Jobsite Jobs','Perfect Placement','ARRAY','JOBG8','Matchtech Group plc.','Penguin Recruitment','Randstad','Adecco','Michael Page Finance','Adecco Group','BMS Sales Specialists LLP','COREcruitment International','Page Personnel Finance'}:
	count=salary=av_slr=0
	for i in list_cpn:
		if i[0] == j:
			count+=1
			salary+=i[1]
	av_slr=int(salary/count)
	cpn1.append(j)
	cpn_slr1.append(av_slr)

cpn_dict1=dict(zip(cpn1,cpn_slr1))
cpn_dict2=dict(sorted(cpn_dict1.items(), key = lambda x:x[1],reverse = False))
cpn2=list(cpn_dict2.keys())
cpn_slr2=list(cpn_dict2.values())
print(cpn_dict2)
print(cpn2)
print(cpn_slr2)

for j in {'UK','London','South East London','The City','Manchester','Leeds','Birmingham','Central London','West Midlands','Surrey','Reading','Bristol','Nottingham','Sheffield','Aberdeen','Hampshire','Belfast','East Sheen','Milton Keynes','Berkshire'}:
	count=salary=av_slr=0
	for i in list_lct:
		if i[0] == j:
			count+=1
			salary+=i[1]
	av_slr=int(salary/count)
	cpn1.append(j)
	cpn_slr1.append(av_slr)

cpn_dict1=dict(zip(cpn1,cpn_slr1))
cpn_dict2=dict(sorted(cpn_dict1.items(), key = lambda x:x[1],reverse = False))
cpn2=list(cpn_dict2.keys())
cpn_slr2=list(cpn_dict2.values())
print(cpn_dict2)
print(cpn2)
print(cpn_slr2)
