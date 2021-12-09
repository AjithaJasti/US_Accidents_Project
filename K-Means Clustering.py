from sklearn.cluster import MiniBatchKMeans
from folium.plugins import HeatMap
import folium
import numpy as np 
import pandas as pd 


usaccidents = pd.read_csv("gs://usaaccidents/US-Accidents/US_Accidents.csv")
for c in usaccidents.columns:
    if usaccidents[c].dtype==bool:
        usaccidents[c]=usaccidents[c].astype('int')
        
dt=np.array(usaccidents[{'Start_Lat','Start_Lng'}])


kmeans = MiniBatchKMeans(n_clusters=100, random_state=10, batch_size=10240, verbose=3)
start=0
while start<len(dt):
    if start+10240>len(dt):
        kmeans.partial_fit(dt[start:,:])
    else:
        kmeans.partial_fit(dt[start:start+10240,:])
    start+=10240
kmeans.cluster_centers_


map = folium.Map()
HeatMap(kmeans.cluster_centers_).add_to(map)
map