import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file="/Users/azeman/Desktop/Study UCD/Final Project UCDPA/Olympics archive/athlete_events.csv"
olympics_data=pd.read_csv(file, sep=',', comment='#')

#first we want to know the shape: it shows 271116 rows and 15 columns
print(olympics_data.shape)

#next we want to know what the columns entail
print(olympics_data.columns)

#and a general overview: 271116 rows x 15 columns
print(olympics_data.info)
print(olympics_data.head(10))

#we check how many unique ID there are: 135571
print (len(olympics_data.ID.unique()))

#we'd like an overview of missing values and show it in a bar-graph
print (olympics_data.isna().any())
olympics_data.isna().sum().plot(kind='bar')
plt.show()

#we can see we have missing values in Age, Height, Weight and Medal. Need to clean these if we are going to use them



#I found a way to mark the 18th row, and by going into the debugger, check how to see the code as a dataframe//
#there we found that the row
committing this
#here is some more text, lets check it is pushed