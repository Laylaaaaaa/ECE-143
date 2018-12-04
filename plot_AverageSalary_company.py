import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import cm
import matplotlib
from matplotlib.cm import ScalarMappable

cpn1=['Office Angels', 'Page Personnel Finance', 'Adecco', 'Adecco Group', 'Perfect Placement', 'Penguin Recruitment', 'ARRAY', 'Hays', 'CVbrowser', 'COREcruitment International', 'UKStaffsearch', 'Randstad', 'Jobsite Jobs', 'London4Jobs', 'BMS Sales Specialists LLP', 'Michael Page Finance', 'JAM Recruitment Ltd', 'JOBG8', 'Matchtech Group plc.']
slr1=[20205, 21814, 22013, 22097, 25267, 27803, 29000, 31333, 32338, 34077, 34462, 37150, 39092, 39812, 40068, 43765, 43815, 44138, 44291]
data_color = [x / max(slr1) for x in slr1]

my_cmap = plt.cm.get_cmap('RdPu')
colors = my_cmap(data_color)
sm = ScalarMappable(cmap=my_cmap,norm=plt.Normalize(0, vmax=max(slr1)))
sm.set_array([])
cbar = plt.colorbar(sm)

width=0.7
plt.barh(cpn1,slr1,width,color=colors)
plt.xlabel('Average Salary')
plt.ylabel('Company')
plt.title('Average Salary per Company',fontsize=16)
plt.show()