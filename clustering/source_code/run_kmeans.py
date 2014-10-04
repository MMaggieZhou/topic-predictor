from time import time
import numpy as np
import csv
from numpy import genfromtxt
from kmeans import clustering

source = "/Users/mengqizhou/Desktop/datamining/programing3/data/initialdata/weighted_vectors.csv"
vector = genfromtxt(source, dtype=float,delimiter = ',')
vector = np.array(vector)
for i in range(0,len(vector)):
            vector[i][1]+=0.1
file1="/Users/mengqizhou/Desktop/datamining/programing3/data/centroid/sample_cosine_200.csv"
file2="/Users/mengqizhou/Desktop/datamining/programing3/data/centroid/sample_euclidean_127.csv"
for iteration in range(0,2):
    if iteration==0:
        seed = genfromtxt(file1, dtype=float,delimiter = ',')
        seed = np.array(seed)       
        for i in range(0,len(seed)):
            seed[i][1]+=0.1
        t=time()
        mean,vnoc,nvoc= clustering(vector,seed,'cosine')
        print"cosine,"+str(len(mean))+" clusters,time: "+str(time()-t)+" s"
        np.savetxt("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/centroid/cosine_"+str(len(mean))+".csv", mean, '%5.2f',delimiter=",")
        with open("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/vnoc/cosine_"+str(len(vnoc))+".csv", 'wb') as f:
            writer=csv.writer(f)
            for item in vnoc:
                writer.writerow(item)
        f.close()
        np.savetxt("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/nvoc/cosine_"+str(len(nvoc))+".csv", nvoc, '%i',delimiter=",")
    elif iteration==1:
        seed = genfromtxt(file2, dtype=float,delimiter = ',')
        seed = np.array(seed)
        for i in range(0,len(seed)):
            seed[i][1]+=0.1
        t=time()
        mean,vnoc,nvoc= clustering(vector,seed,'euclidean')
        print "euclidean,"+str(len(mean))+" clusters,time: "+str(time()-t)+" s"
        np.savetxt("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/centroid/euclidean_"+str(len(mean))+".csv", mean, '%5.2f',delimiter=",")
        with open("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/vnoc/euclidean_"+str(len(vnoc))+".csv", 'wb') as f:
            writer=csv.writer(f)
            for item in vnoc:
                writer.writerow(item)
        f.close()
        np.savetxt("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/nvoc/euclidean_"+str(len(nvoc))+".csv", nvoc, '%i',delimiter=",")