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
print(('the Shape of the Olympics data-set is'),olympics_data.shape)

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
print(total_data.columns)

#First I wanted to check the amount of duplicate values in the dataset. There are 1385 rows in total that are duplicates.
duplicate_rows = total_data[total_data.duplicated()]
print(duplicate_rows)
print (duplicate_rows.shape)

#Next we want to drop the duplicates, and make sure the duplicates are indeed dropped.
total_data.drop_duplicates(inplace=True)

duplicate_rows2 = total_data[total_data.duplicated()]
print (duplicate_rows2)
print (duplicate_rows2.shape)

#we would like an overview of missing values and show it in a bar-graph
print (total_data.isna().any())
total_data.isna().sum().plot(kind='bar')
plt.show()

#making a function to measure the percentage of NaN values and looping
def None_as_percentage(total_data, column_name):
    rows_count = total_data[column_name].shape[0]
    empty_values = rows_count - total_data[column_name].count()
    return (100.0*empty_values)/rows_count
for i in list(total_data):
    print(i +': ' + str(None_as_percentage(total_data,i))+'%')

#We can see we have missing values in Age, Height, Weight and Medal. Need to clean these if we are going to use them
#First we calculate the mean and  median age
mean_age=total_data["Age"].mean()
print (('the mean age is:'), mean_age)
median_age=total_data["Age"].median()
print (('the median age is:'), median_age)

#then we fill the median age in the Age column for the values that are null
total_data["Age"]=total_data["Age"].fillna(median_age)

#We check the values, see if the change is made
print (total_data.isnull().sum())
print (None_as_percentage(total_data, ["Age"]))

#we do the same for the 'Height'
mean_height=total_data["Height"].mean()
print (('the mean height is'),mean_height)
#then we fill the mean height in the Height column for the values that are null
total_data["Height"]=total_data["Height"].fillna(mean_height)
total_data["Height"]
#We check the values, see if the change is made
print (total_data.isnull().sum())

#we do the same for the 'Weight'
mean_weight=total_data["Weight"].mean()
print ('the mean weight is', mean_weight)

#then we fill the mean weight in the Weight column for the values that are null
total_data["Weight"]=total_data["Weight"].fillna(mean_weight)
total_data["Weight"]

#We check the values, see if the change is made
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


#We go on to grouping by Sex and see how many participants each Sex had
data_gender=total_data['Sex'].value_counts()
print (data_gender.head())
g = sns.catplot(x=total_data['Sex'], data=total_data, kind="count")
plt.xlabel("Male and Female participation")
plt.ylabel("Participants")
plt.show()

#We checked the distribution across Sex for Height
sns.set_style('whitegrid')
g = sns.catplot(x = total_data['Sex'],
            y = "Height",
            data = total_data,
            kind = "box",
            sym="")
g.fig.suptitle('Boxplot of Male and Female height in Olympics history', y=1.00)
plt.show()

#We checked the distribution across Sex for Weight
g = sns.catplot(x = total_data['Sex'],
            y = "Weight",
            data = total_data,
            kind = "box",
            sym="")
g.fig.suptitle('Boxplot of Male and Female weight in Olympics history', y=1.00)
plt.show()

#And finally we checked the distribution across Sex for Age
g = sns.catplot(x = total_data['Sex'],
            y = "Age",
            data = total_data,
            kind = "box",
            sym="")
g.fig.suptitle('Boxplot of Male and Female Ages in Olympics history', y=1.00)
plt.show()

#We now want to see how many participants there were per edition
IDgroupedbyyear = total_data.groupby(['Year','ID'],as_index=False).count()[['Year','ID']]
IDgroupedbyyear = IDgroupedbyyear.groupby('Year',as_index=False).count()
print (IDgroupedbyyear.head())

#Now let's get the sum
IDgroupedbyyear = IDgroupedbyyear.groupby('Year',as_index=False).sum()

#And show it as a plot
sns.set_context("paper")
sns.set(rc={'figure.figsize':(14,8)})
g=sns.catplot(x="Year", y="ID",
            data=IDgroupedbyyear, kind="bar")
g.fig.suptitle("Participants per event", y=1.00)
plt.ylabel("Participants")
plt.xticks(rotation=90)
plt.show()

#I wanted to do it in another way
winners_by_age = sns.barplot(x='Year',y='ID',data=IDgroupedbyyear).set_xticklabels(IDgroupedbyyear.Year,rotation=45)
plt.xlabel("Year")
plt.ylabel("Participants")
plt.show()

#I would like to know the distribution of gold medals over the age
gold_medals = total_data[(total_data.Medal == 'Gold')]
gold_medals.head()
plt.figure(figsize=(14, 8))
plt.tight_layout()
sns.countplot(x=gold_medals['Age'])
plt.xticks(rotation=45)
plt.title('Age distribution of Gold Medals')
plt.show()

print (gold_medals['Sport'][gold_medals['Age'] > 50])
ancient_olympians = gold_medals['Sport'][gold_medals['Age'] > 50]

plt.figure(figsize=(14, 8))
plt.tight_layout()
sns.countplot(x=ancient_olympians, order = ancient_olympians.value_counts().index)
plt.title('Sports with Gold Medals for athletes over 50')
plt.show()

#Changing to numpy array
np_height = total_data['Height'].to_numpy()
print(type(np_height))
avg_height = np.mean(np_height)
print("Average: " + str(avg_height) + ' cm')
med_height = np.median(np_height)
print("Median: " + str(med_height)+ ' cm')

np_weight = total_data['Weight'].to_numpy()
print(type(np_weight))
avg_weight = np.mean(np_weight)
print("Average: " + str(avg_weight) + ' kg')
med_weight = np.median(np_weight)
print("Median: " + str(med_weight) + ' kg')

bmi = np_weight / np_height ** 2
real_bmi = bmi * 10000
print (real_bmi)
print (type(real_bmi))

light = real_bmi < 18
print (light)

#real_bmi is a numpy.ndarray, and I want to convert this to a list
list_bmi = np.array([real_bmi]).tolist()
print (type(list_bmi))