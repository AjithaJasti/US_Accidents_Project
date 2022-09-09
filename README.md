# US_Accidents_Project

# Abstract 

This is a countrywide data set consisting of data collected between 2016-2020 and contains 1.5 million data records. The purpose of this data analysis is to find the cause and severity of accidents and reduce the loss. The first objective is to visualize the data using EDA to better understand the severity. The algorithms used are K-means Clustering and Reservoir Sampling. Using these approaches we found the highest accidents occurring time and the most dangerous place. So that we might be able to allocate better financial and human resources. 

# Motivation 
Every year multiple accidents take place. The economic and societal impact of traffic accidents cost U.S. citizens hundreds of billions of dollars every year. To reduce accidents, we need to understand numerous applications such as real-time car accident prediction, casualty analysis and extracting cause and effect rules to predict car accidents, and studying the impact of environmental stimuli on accident occurrence. 
Goals 
➔ To determine what time of day has the highest probability of accidents ➔ To determine the month and day of the highest accidents. 
➔ To determine what parts of the road are most dangerous (freeway, city driving,
etc) 
➔ To determine which state has the highest risk for accidents. 

# Data Set 
➔ This is a countrywide traffic accident dataset, which covers 49 states of the United States. 
➔ The data is continuously being collected from February 2016, using several data providers, including multiple APIs that provide streaming traffic event data. ➔ These APIs broadcast traffic events captured by a variety of entities, such as the US and state departments of transportation, law enforcement agencies, traffic cameras, and traffic sensors within the road networks. 
➔ Currently, there are about 1.5 million accident records in this dataset and 47 columns. 
➔ Each accident record consists of a variety of intrinsic and contextual attributes such as location, time, natural language description, weather, period of the day, and points of interest. 

# Exploratory Data Analysis 
➢ The primary goal of EDA is to maximize the analyst's insight into the underlying structure of the dataset to summarize their main characteristics, using statistical graphics and other data visualization methods. 
➢ The EDA below has been used to visualize the following: 
○ Finding the time, day and month where the accident rate percentage is high. 
○ The highest state and the parts have the highest probability of occurrence. ○ Percent of accidents that occured at Junctions, Traffic Signals, and Crossings.

# Algorithms Used 
➢ A Reservoir sampling algorithm was used for the purpose of running different pieces of code faster while in the development process. All of the information seen within this document uses the full dataset. The dataset used includes about 2 million rows and 20 columns. We opted for a random sample of K = 5000 rows, and the columns depended on what was being researched. K is adjustable within the program. 
➢ The K-means algorithm is to visualize the dangerous place more precisely ○ Because the dataset is large, it did not use Hierarchical clustering, and MiniBatchKMeans() was used to speed up the running time. 
➢ The Map below visualizes groupings of where most accidents are occurring

# Findings 
Around 5 P.M of time has the highest probability of accidents. 
December is the highest and July is the lowest month of accident rate 
The day which has the highest percentage of accidents is Thursday, with Sunday being the lowest. 
California has the highest risk for accidents of all the states. 
Los Angeles has the highest risk for accidents of all the cities. 
Most accidents do not occur in city-like situations, such as junctions or stop lights. 
The only issue with the results we found in the project is attributed to the collection of the data itself. The data includes results from 49 states, which is excluding Alaska. Our whole project greatly depends on the accuracy and evenness of the researcher’s data collection. However, our results appear to be consistent with that of other studies. 

# Conclusions 
The results seen in our analysis reveal some interesting information about the circumstances in which accidents are likely to occur, and where. We can see that most Accidents happen outside of junctions, and in population centres- specifically in California. And even more specifically - Los Angeles. We also see the time when accidents are most likely. Overall, 5 pm is a common time for a lot of accidents and Thursday is the most dangerous day. 
If we were to do this project again, we would attempt to find any patterns that may have revealed associations between different causes of accidents. For example, perhaps we
may have found some association between poor weather and more accidents occurring in city-like environments. 

