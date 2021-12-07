import pandas as pd
import random

criteria = ['ID', 'Severity', 'State', 'Temperature(F)']
sizeOfRes = 30


def createResDf(reservoir, df, k):
    resDf = pd.DataFrame(columns=criteria)
    for i in reservoir:
        resDf = resDf.append(df.loc[i], ignore_index = False)
    return resDf

def selectKItems(stream, n, k):
    i=0
    reservoir = [0]*k
    for i in range(k):
        reservoir[i] = stream[i]
    while(i < n):
        j = random.randrange(i+1)
        if(j < k):
            reservoir[j] = stream[i]
        i+=1;

    return reservoir

if __name__ == "__main__":
        filename = r'C:\Users\aidan\Downloads\US_Accidents_Project-main\US_Accidents_Project-main\US_accidents.csv'
        data = pd.read_csv(filename)
        df = pd.DataFrame(data, columns=criteria)

        z = (sum(1 for line in open(filename)) -1)
        stream = [*range(0, z)]
        n= len(stream)
        k = sizeOfRes
        reservoir = selectKItems(stream, n, k)
        resDf = createResDf(reservoir, df, k)
        print("Our new reservoir:")
        print(resDf)

        
