# Description
This is UCSD ECE143 final project created by Group 3.<br>
We used the Kaggle [Job Salary Prediction](https://www.kaggle.com/c/job-salary-prediction/data) dataset and applied what we learn during the class.

# Database
The dataset contains over 200,000 data points with features: Id, Title, FullDescription, LocationRaw, LocationNormalized, ContractType, ContractTime, Company, Category and SourceName.

# Requirements
1. Packages
   - Please install following packages:
     - plotly
     - pyecharts
     - wordcloud
     - seaborn
     - pandas
     - csv
     - matplotlib
     - Numpy
     - BaseMap
     - Image
2. Juypter Notebook

# Quick Start
- If you want to quickly get an overview about what we have done in this project, you can open **ECE_143_Project.ipynb** directly to see  our result or just look at our **ECE_143_Prensentation Slides.pptx**.
- If you really want to know how do we run the code, you can download the dataset and the folder **ECE_143_Jupyter**. Put all of them together and run on Juypter Notebook.
- If you still want to dig a little more about our code, we'll recommend you to look at **Functions and code descriptions** below 
. It's including descriptions of all the funcitons and analysis and the functions are in the folder **Function Code**

# Functions and code descriptions:
  
- color_map_AverageSalary.py:<br>
    Read data from "Train_rev1.csv" and classify salary by locations and read classification of UK city from gadm36_GBR_3.
    Generate UK map and color this map by average salary of locations.
    Should install csv, matplotlib, Numpy and BaseMap in Python.

- color_map_NumOfJob.py:<br>
    Read data from Train_rev1.csv and count number of job of locations and read classification of UK city from gadm36_GBR_3.
    Generate UK map and color map by number of job of locations.
    Should install csv, matplotlib, Numpy and BaseMap in Python.
  
- color_map_JObCategory.py:<br>
    Read data from Train_rev1.csv and count number of IT, Engineer and Finance job of locations and read classification of UK city from gadm36_GBR_3.
    Generate UK map and color map by number of Engineer job of locations.
    Should install csv, matplotlib, Numpy, Image and BaseMap in Python.
    
- Result Map.html:<br>
    It is based on Google map API and generates a dynamic map about job information of a location.
    Information includes average salary, the most common job category and the number of jobs of a location.

- read_data_from_excel.py:<br>
    Read data from Train_rev1.csv and determines the overall statistics of the dataset. It gets the average
    and max salary per category and also determines the average salary across the entire dataset. This module
    also predicts the type of company based off the number of job category listings that there are.
    Generates a bar chart of the number of job listing per each category of job
    
- Average Salary_category_company_location.py:<br>
    Read data from Train_rev1.csv with distinct keys.(company/category/location)
    It calculates average salary for each company/category/location.
    Should install csv, matplotlib, numpy and pandas.
    
- plot_AverageSalary_category.py<br>
    Plot bar chart with average salary for each category.
    Should install matplotlib, seaborn.
    
- plot_AverageSalary_company.py<br>
    Plot bar chart with average salary for each company.
    Should install matplotlib, seaborn.
    
- self_defined_function.py<br>
     Plot the line chart, box plot, top 20 categories in the demonstration of **ECE_143_Project.ipynb**
