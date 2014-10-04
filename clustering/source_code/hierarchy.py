from numpy import genfromtxt
import numpy as np
from scipy.cluster import hierarchy as h
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
from time import time
folder="/Users/mengqizhou/Desktop/datamining/programing3/data/clustering/"
sample = "/Users/mengqizhou/Desktop/datamining/programing3/data/initialdata/weighted_sample.csv"
file1="/Users/mengqizhou/Desktop/datamining/programing3/data/initialdata/weighted_vectors.csv"

numpyA = []
numpyA = genfromtxt(file1, dtype=float,delimiter = ',')
numpyA = np.array(numpyA)
for i in range(0,len(numpyA)):
        numpyA[i][1]+=0.1
for i in range(0,2):
    t1 = time()
    if i ==0:
        y=pdist(numpyA,'cosine')
        a=max(y)
        b=min(y)
        y=squareform(y)
        for k in range(0,len(y)):
            for j in range(0,len(y[0])):
                y[k][j]= ((y[k][j]-b)/(a-b))+b        
    elif i ==1:
        y=pdist(numpyA,'euclidean')
        y=squareform(y)    
    z=h.centroid(y)
    if i==0: print "cosine, hierarchy clustering time = "+str(time()-t1)
    elif i==1: print "euclidean, hierarchy clustering time = "+str(time()-t1)
    
    if i ==0:
        np.savetxt("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy_label/cosine_linkage.csv", z, '%5.2f',delimiter=",")
    elif i==1: np.savetxt("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy_label/euclidean_linkage.csv", z, '%5.2f',delimiter=",")
    j = 4
    while(j<129):

        result = h.fcluster(z, z[len(z)-j][2],'distance')
        if i==0:
            np.savetxt("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy_label/cosine_"+str(j)+".csv", result, '%i',delimiter=",")
        elif i==1:
            np.savetxt("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy_label/euclidean_"+str(j)+".csv", result, '%i',delimiter=",")
        j*=2