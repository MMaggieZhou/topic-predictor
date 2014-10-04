import numpy as np
import csv
from numpy import genfromtxt
from merge import merge

source = "/Users/mengqizhou/Desktop/datamining/programing3/data/initialdata/weighted_vectors.csv"
vector = genfromtxt(source, dtype=float,delimiter = ',')
vector = np.array(vector)
for i in range(0,len(vector)):
            vector[i][1]+=0.1
vnoc1="/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/vnoc/cosine_200.csv"
centroid1="/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/centroid/cosine_200.csv"
nvoc1="/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/nvoc/cosine_200.csv"
vnoc2="/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/vnoc/euclidean_125.csv"
centroid2="/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/centroid/euclidean_125.csv"
nvoc2="/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/nvoc/euclidean_125.csv"

for iteration in range(0,2):
    vnoc=[]
    if iteration==0:        
        with open(vnoc1,'rU') as f:
                reader = csv.reader(f)
                for row in reader:
                    vnoc.append(row)
        f.close()
        mean = genfromtxt(centroid1, dtype=float,delimiter = ',')
        nvoc=genfromtxt(nvoc1, dtype=int,delimiter = ',')
    if iteration==1:
        with open(vnoc2,'rU') as f:
                reader = csv.reader(f)
                for row in reader:
                    vnoc.append(row)
        f.close()
        mean = genfromtxt(centroid2, dtype=float,delimiter = ',')
        nvoc=genfromtxt(nvoc2, dtype=int,delimiter = ',')
    temps=[]
    for row in vnoc:
        temp=[]
        for value in row:
            if value!='':
                temp.append(value)
        temps.append(temp)
    vnoc=temps
    temps=[]
    for item in vnoc:
        temps.append(map(int,item))
    vnoc=temps
    if iteration==0:
        merge(vnoc,mean,nvoc,4,'cosine',vector)
    elif iteration==1:
        merge(vnoc,mean,nvoc,4,'euclidean',vector)