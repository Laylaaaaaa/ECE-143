# Description
This is UCSD ECE143 final project develeped by Group 3.<br>
We use Kaggle [Job Salary Prediction](https://www.kaggle.com/c/job-salary-prediction/data) and try to aplly what we learn during the class.
# Database
The dataset contains 200 thousand more data points with heads: Id, Title, FullDescription, LocationRaw, LocationNormalized, ContractType, ContractTime, Company, Category and SourceName.

# Requirements
1. Packages
   -Please install following packages:
    -plotly
    -pyecharts
    -wordcloud
2.
    
# Functions and code description:
  
-color_map_AverageSalary.py:
    Read data from "Train_rev1.csv" and classify salary by locations.
    Generate UK map and color this map by average salary of locations.
    Should install csv, matplotlib, Numpy and BaseMap in Python.

-color_map_NumOfJob.py:
    Read data from Train_rev1.csv and count number of job of locations.
    Generate UK map and color map by number of job of locations.
    Should install csv, matplotlib, Numpy and BaseMap in Python.
  
-Result Map.html:
    It is based on Google map API and generates a dynamic map about job information of a location.
    Information includes average salary, the most common job category and the number of jobs of a location.
