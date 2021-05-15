import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file="/Users/azeman/Desktop/Study UCD/Final Project UCDPA/Olympics archive/athlete_events.csv"
olympics_data=pd.read_csv(file, sep=',', comment='#')

#We can now add the second dataset
regions_NOC=pd.read_csv('/Users/azeman/Desktop/Study UCD/Final Project UCDPA/Olympics archive/noc_regions.csv')

#first we want to know the shape of the first data set: it shows 271116 rows and 15 columns
print(('the Shape of the Olympics data-set is'), olympics_data.shape)

#next we want to know what the columns entail
print(olympics_data.columns)

#and a general overview: 271116 rows x 15 columns
print(olympics_data.info)
print(olympics_data.head(10))

#we check how many unique ID there are: 135571
print (("amount of unqiue athletes participating in the olympics is;"), len(olympics_data.ID.unique()))

#Next we check the data of the second data set; 230 rows x 3 columns, Index(['NOC', 'region', 'notes']
print (('the Shape of the regions NOC dataset is'), regions_NOC.shape)
print(regions_NOC.head)
print(regions_NOC.columns)

#we can now merge the 2 datasets into total_data
total_data = pd.merge(olympics_data, regions_NOC, left_on='NOC', right_on='NOC')
print ('total_data')
print(total_data.columns)
print ('total_data end of columns')

#making a function to measure the percentage of NaN values
print ('trying new code out')
def NaN_percent(total_data, column_name):
    rows_count = total_data[column_name].shape[0]
    empty_values = rows_count - total_data[column_name].count()
    return (100.0*empty_values)/rows_count
for i in list(total_data):
    print(i +': ' + str(NaN_percent(total_data,i))+'%')
print ('en of trying new code out')

#we'd like an overview of missing values and show it in a bar-graph
print (total_data.isna().any())
total_data.isna().sum().plot(kind='bar')
plt.show()


#We can see we have missing values in Age, Height, Weight and Medal. Need to clean these if we are going to use them
#First we calculate the mean age
mean_age=total_data["Age"].mean()
print ('the mean age is')
print (mean_age)

#then we fill the mean age in the Age column for the values that are null
total_data["Age"]=total_data["Age"].fillna(mean_age)
total_data["Age"]

#We check the values, see if the change is made
print (total_data.isnull().sum())


#we do the same for the 'Height'
mean_height=total_data["Height"].mean()
print ('the mean height is')
print (mean_height)
#then we fill the mean height in the Height column for the values that are null
total_data["Height"]=total_data["Height"].fillna(mean_height)
total_data["Height"]
#We check the values, see if the change is made
print (total_data.isnull().sum())

#we do the same for the 'Weight'
mean_weight=total_data["Weight"].mean()
print ('the mean weight is')
print (mean_weight)



#then we fill the mean weight in the Weight column for the values that are null
total_data["Weight"]=total_data["Weight"].fillna(mean_weight)
total_data["Weight"]

#We check the values, see if the change is made
print (total_data.isnull().sum())
print ('We have now cleaned the Age, Weight and Height columns')
print (total_data.isnull().sum())
print(total_data.isna().any())
total_data.isna().sum().plot(kind='bar')
plt.show()



#We now want to change the NaN values in the Medals column to Losers
total_data['Medal'] = total_data['Medal'].fillna('Losers')
print (total_data.isnull().sum())

#We check the values, see if the change is made
print (total_data.isna().any())
total_data.isna().sum().plot(kind='bar')
plt.show()

print (total_data.head)
print(total_data.columns)
print (type(total_data))

#We go on to grouping by Sex
data_gender=total_data['Sex'].value_counts()
print (data_gender.head())
#data_gender.sum().plot(kind='bar')
#plt.show()


#Now we are going to see how many participants the Netherlands had in each Games
Netherlands_edition_grouped = total_data.loc[total_data.NOC == 'NED'].groupby('Games')
print (Netherlands_edition_grouped['Medal'].count().head())

Netherlands_edition_grouped['Medal'].count().plot(kind='bar', rot=45)
plt.xlabel('Games')
plt.ylabel('Amount of medals')
plt.title('Amount of participants by the Netherlands per Edition')
plt.show()


#Now we are going to see how many medals the Netherlands won in each Games
Netherlands_edition_grouped_medals = olympics_data.loc[olympics_data.NOC == 'NED'].groupby('Games')
print (Netherlands_edition_grouped_medals['Medal'].count().head())

Netherlands_edition_grouped_medals['Medal'].count().plot(kind='bar', rot= 45)
plt.xlabel('Games')
plt.ylabel('Amount of participants')
plt.title('Amount of Medals won by the Netherlands per Edition')
plt.show()


#We now want to see how many participants there were per edition
IDgroupedbyyear = total_data.groupby(['Year','ID'],as_index=False).count()[['Year','ID']]
IDgroupedbyyear = IDgroupedbyyear.groupby('Year',as_index=False).count()
IDgroupedbyyear.head()

#Now let's get the sum
IDgroupedbyyear = IDgroupedbyyear.groupby('Year',as_index=False).sum()

sns.set(rc={'figure.figsize':(18,12)})
plot1 = sns.barplot('Year','ID',data=IDgroupedbyyear).set_xticklabels(IDgroupedbyyear.Year,rotation=45)
#plot1.set(xlabel='YEAR',ylabel='Number of people')
plt.xlabel("YEAR")
plt.ylabel("PARTICIPANTS")
plt.show()




#Changing to numpy array

np_height = total_data['Height'].to_numpy()
print(type(np_height))
print(np.mean(np_height))
print (np.median(np_height))
avg = np.mean(np_height)
print("Average: " + str(avg))
med = np.median(np_height)
print("Median: " + str(med))



np_weight = total_data['Weight'].to_numpy()
print(type(np_weight))
print(np.mean(np_weight))
print (np.median(np_weight))
avg = np.mean(np_weight)
print("Average: " + str(avg))
med = np.median(np_weight)
print("Median: " + str(med))

#we're gonna creat the function BMI
#np_height = np.array(height)
#np_weight = np.array(weight)

bmi = np_weight / np_height ** 2
print (bmi)


#total_data.plot("Year", "Team")
#plt.show()


##The 'Games' column is just the 'Year' and 'Season' column combined
#new_olympics_data = olympics_data.drop(['Games'], axis = 1)
#new_total_data = total_data.drop(['Notes', 'Games']), axis = 1)
#print (new_total_data.head)
#print(new_total_data.columns)

#we'd like an overview of missing values and show it in a bar-graph
#print (new_total_data.isna().any())
#new_total_data.isna().sum().plot(kind='bar')
#plt.show()

#we are now going to count the missing values: missing_values = olympics_data.isnull().sum()
#print(new_olympics_data.isnull().sum())



#print (olympics_data_medals.isna().any())
#print(olympics_data_medals.shape)
#print(olympics_data_medals.columns)


#I found a way to mark the 18th row, and by going into the debugger, check how to see the code as a dataframe//
#there we found that the row