# assignment-2 on pandas
#Import Python Libraries
import numpy as np
import pandas as pd
# reading a file
#import the data by Reading from csv file
df = pd.read_csv("C:/Users/user/Desktop/python learning/JNTUK/50_Startups.csv")
df.head()
df.columns
df.shape
# slicing first 15 rows into data1
data1=df[:15]
data1.shape
#administration column only
admin=df['Administration']
admin.head()
# c)	Finding min, max, head, tail, dtypes values of Administration column.
admin.min()
admin.max()
admin.head()
admin.tail()
# Slicing 2 & 3 columns of the data frame and store it into another variable.
data2=df.iloc[:, 2:4]
data2.head()
data2.tail()
'''
Find out the aggregations like mean, median,variance and standard deviation
 for first 20 rows of profit column
'''
profit_col=df.iloc[:20,4:5]
profit_col.head()
profit_col.tail()
profit_col.median()
profit_col.mean()
profit_col.std()
#Find out the profit median for different states.Use groupby function
df_state = df.groupby(['State'])
df_state['Profit'].median()
#Filter out the rows from dataframe where R&D Spend is more than 50,000
sel_rows=df[df['R&D Spend']>50000]
sel_rows.shape
sel_rows.head()

