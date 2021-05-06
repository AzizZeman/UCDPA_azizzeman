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

#The 'Games' column is just the 'Year' and 'Season' column combined
new_olympics_data = olympics_data.drop(['Games'], axis = 1)

print (new_olympics_data.head)
print(new_olympics_data.columns)

#we'd like an overview of missing values and show it in a bar-graph
print (new_olympics_data.isna().any())
new_olympics_data.isna().sum().plot(kind='bar')
plt.show()

#we are now going to count the missing values: missing_values = olympics_data.isnull().sum()
print(new_olympics_data.isnull().sum())

#We can now add the second dataset
regions_NOC=pd.read_csv('/Users/azeman/Desktop/Study UCD/Final Project UCDPA/Olympics archive/noc_regions.csv')

#check the first data; 230 rows x 3 columns, Index(['NOC', 'region', 'notes']
print(regions_NOC.head)
print(regions_NOC.columns)

#we can now merge the 2 datasets into total_data
total_data = pd.merge(new_olympics_data, regions_NOC, left_on='NOC', right_on='NOC')
print ('total_data')
print(total_data.columns)
print ('total_data end of columns')



#we can see we have missing values in Age, Height, Weight and Medal. Need to clean these if we are going to use them
olympics_data_height=total_data['Height'].fillna(olympics_data['Height'].mean(), inplace = False)
print(olympics_data_height.isnull().sum())


#we can see we have missing values in Age, Height, Weight and Medal. Need to clean these if we are going to use them

print('olympics data medals 1')
olympics_data['Medal'].fillna(olympics_data["Loser"], inplace = False)
print(olympics_data_medals.columns)
print (olympics_data_medals.head())
print('olympics data medals 2')


print (olympics_data.isna().any())
new_olympics_data.isna().sum().plot(kind='bar')
plt.show()

#print (olympics_data_medals.isna().any())
#print(olympics_data_medals.shape)
#print(olympics_data_medals.columns)



#I found a way to mark the 18th row, and by going into the debugger, check how to see the code as a dataframe//
#there we found that the row

#here is some more text, lets check it is pushed

print (olympics_data_medals.isna().any())
print (olympics_data_medals.isnull().sum())
print (olympics_data_medals)