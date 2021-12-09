import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


#Reading the Data
usaccidents = pd.read_csv("gs://usaaccidents/US-Accidents/US_Accidents.csv")
print(usaccidents.head())

print(usaccidents.info())

total_missing = usaccidents.isna().sum().sort_values()
total_missing[total_missing != 0].plot(kind='barh')

#Total number of states
states = usaccidents["State"].unique()
print("Total number of states= ",len(states))

#Top 5 states with highest accidents
total_state_accidents = usaccidents.State.value_counts()
print("Top 5 states with highest accidents")

fig, ax = plt.subplots(figsize = (23,7))
state_plot = sns.countplot(x=usaccidents.State, data=usaccidents,color="#508484")
state_plot.set_title("No. of Accidents by State")
state_plot

#Top 10 states most affected by Accidents
plt.pie(total_state_accidents[:10].values, labels = total_state_accidents[:10].index,startangle=90, shadow = True,autopct = '%1.1f%%')
plt.title("Top 10 states most affected by Accidents")
plt.show()


city = usaccidents["City"].unique()
print("Total number of Cities= ",len(city))
city

#Top 5 cities with highest accidents
total_city_accidents = usaccidents["City"].value_counts()
print("Top 5 cities with highest accidents")
total_city_accidents[:5]


#Top 10 cities most affected by Accidents
plt.pie(total_city_accidents[:10].values, labels = total_city_accidents[:10].index,startangle=90, shadow = True,autopct = '%1.1f%%')
plt.title("Top 10 cities most affected by Accidents")
plt.show()


fig, ax = plt.subplots(figsize = (20,5))
city_plot = sns.countplot(x=usaccidents.City, data=usaccidents, order=usaccidents.City.value_counts().iloc[:50].index, orient = 'v', color = "#4ECDC4")
city_plot.set_title("No. of Accidents by City - Top 50 cities")
city_plot.set_xticklabels(city_plot.get_xticklabels(), rotation=90)
city_plot

counts = pd.to_datetime(usaccidents['Start_Time']).dt.day_name().value_counts()
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

plt.figure(figsize=(20, 8))
plt.title("Number of accidents for each weekday")
sns.barplot(counts.index, counts.values, order=weekdays)
plt.xlabel("Weekday")
plt.ylabel("Value")
plt.show()

usaccidents.Start_Time

usaccidents.Start_Time = pd.to_datetime(usaccidents.Start_Time)
usaccidents.Start_Time[0]


# Number of accidents by Hour
fig, ax = plt.subplots(figsize = (10,5))
hour_plot = sns.countplot(x=usaccidents.Start_Time.dt.hour, data=usaccidents, orient = 'v', palette = "rocket")
hour_plot.set_title("No. of Accidents by Hour")
hour_plot


# Number of accidents by Day of the week
dayofweek_plot = sns.countplot(x=usaccidents.Start_Time.dt.dayofweek, data=usaccidents, orient = 'v', palette = "viridis")
dayofweek_plot.set_title("No. of Accidents by day of the week")
dayofweek_plot

# Number of accidents per hour on Sunday
fig, ax = plt.subplots(figsize = (10,5))
sundays_star_time= usaccidents.Start_Time[usaccidents.Start_Time.dt.dayofweek == 6]
dayofweek_plot = sns.countplot(x=sundays_star_time.dt.hour, data=usaccidents, orient = 'v', palette = "magma")
dayofweek_plot.set_title("No. of Accidents per hour on Sundays")
dayofweek_plot

# Number of accidents per hour on Thursday
fig, ax = plt.subplots(figsize = (10,5))
sundays_star_time= usaccidents.Start_Time[usaccidents.Start_Time.dt.dayofweek == 3]
dayofweek_plot = sns.countplot(x=sundays_star_time.dt.hour, data=usaccidents, orient = 'v', palette = "Blues")
dayofweek_plot.set_title("No. of Accidents per hour on Thursdays")
dayofweek_plot

# Number of accidents by month
fig, ax = plt.subplots(figsize = (10,5))
month_plot = sns.countplot(x=usaccidents.Start_Time.dt.month, data=usaccidents, orient = 'v', palette = "light:seagreen")
month_plot.set_title("No. of Accidents by Month")
month_plot

# Number of accidents by year
year_plot = sns.countplot(x=usaccidents.Start_Time.dt.year, data=usaccidents, orient = 'v', palette = "dark:salmon_r")
year_plot.set_title("No. of Accidents by Year")
year_plot