import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import cm
from matplotlib.cm import ScalarMappable

ctg1=['Customer Services', 'Admin', 'Hospitality & Catering', 'Travel', 'Manufacturing', 'Logistics & Warehouse', 'Teaching', 'Sales', 'Social work', 'HR & Recruitment', 'Healthcare & Nursing', 'Retail', 'Other/General', 'PR, Advertising & Marketing', 'Engineering', 'Trade & Construction', 'Consultancy', 'Accounting & Finance', 'Legal', 'IT']
slr1=[19861, 21053, 23702, 23838, 26497, 26497, 27671, 30814, 32381, 32589, 32589, 32955, 35346, 35593, 35838, 36406, 37028, 38751, 42649, 43983]

data_color = [x / max(slr1) for x in slr1]

my_cmap = plt.cm.get_cmap('GnBu')
colors = my_cmap(data_color)
sm = ScalarMappable(cmap=my_cmap,norm=plt.Normalize(0, vmax=max(slr1)))
sm.set_array([])
cbar = plt.colorbar(sm)

width=0.7
plt.barh(ctg1,slr1,width,color=colors)
plt.xlabel('Average Salary')
plt.ylabel('Category')
plt.title('Average Salary per Category',fontsize=16)
plt.show()
