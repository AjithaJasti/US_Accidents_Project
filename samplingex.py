import pandas as pd
import random

if __name__ == '__main__':

    filename = r'C:\Users\aidan\Downloads\US_Accidents_Project-main\US_Accidents_Project-main\US_accidents.csv'
    percentSample = 40


    n = sum(1 for line in open(filename)) -1
    s = n//percentSample

    skip = sorted(random.sample(range(1, n + 1), n - s))

    data = pd.read_csv(filename, skiprows=skip)
    df = pd.DataFrame(data, columns=['ID', 'Severity', 'State', 'Temperature(F)'])
    

    
