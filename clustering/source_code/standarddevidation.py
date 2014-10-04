import entropy
import numpy as np
from numpy import genfromtxt
import csv
vkc=[]#vnoc, kmean, cosine
vkc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/vnoc/cosine_5.csv")
vkc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/vnoc/cosine_8.csv")
vkc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/vnoc/cosine_14.csv")
vkc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/vnoc/cosine_32.csv")
vkc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/vnoc/cosine_93.csv")
vkc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/vnoc/cosine_125.csv")
vke=[]#vnoc,kmean,euclidean
vke.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/vnoc/euclidean_5.csv")
vke.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/vnoc/euclidean_14.csv")
vke.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/vnoc/euclidean_35.csv")
vke.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/vnoc/euclidean_60.csv")
vke.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/vnoc/euclidean_116.csv")
vke.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/vnoc/euclidean_125.csv")
nkc=[]#nvoc, kmean,cosine
nkc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/nvoc/cosine_5.csv")
nkc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/nvoc/cosine_8.csv")
nkc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/nvoc/cosine_14.csv")
nkc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/nvoc/cosine_32.csv")
nkc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/nvoc/cosine_93.csv")
nkc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/nvoc/cosine_125.csv")
nke=[]#nvoc,kmean,euclidean
nke.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/nvoc/euclidean_5.csv")
nke.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/nvoc/euclidean_14.csv")
nke.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/nvoc/euclidean_35.csv")
nke.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/nvoc/euclidean_60.csv")
nke.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/nvoc/euclidean_116.csv")
nke.append("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/nvoc/euclidean_125.csv")
vhc=[]#vnoc,hierarchy,cosine
vhc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/vnoc/cosine_4.csv")
vhc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/vnoc/cosine_8.csv")
vhc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/vnoc/cosine_14.csv")
vhc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/vnoc/cosine_32.csv")
vhc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/vnoc/cosine_93.csv")
vhc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/vnoc/cosine_125.csv")
vhe=[]#vnoc,hierarchy,euclidean
vhe.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/vnoc/euclidean_4.csv")
vhe.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/vnoc/euclidean_8.csv")
vhe.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/vnoc/euclidean_16.csv")
vhe.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/vnoc/euclidean_31.csv")
vhe.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/vnoc/euclidean_116.csv")
vhe.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/vnoc/euclidean_128.csv")
nhc=[]#nvoc,hierarchy,cosine
nhc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/nvoc/cosine_4.csv")
nhc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/nvoc/cosine_8.csv")
nhc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/nvoc/cosine_14.csv")
nhc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/nvoc/cosine_32.csv")
nhc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/nvoc/cosine_93.csv")
nhc.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/nvoc/cosine_125.csv")
nhe=[]#nvoc,hierarchy,cosine
nhe.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/nvoc/euclidean_4.csv")
nhe.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/nvoc/euclidean_8.csv")
nhe.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/nvoc/euclidean_16.csv")
nhe.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/nvoc/euclidean_31.csv")
nhe.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/nvoc/euclidean_116.csv")
nhe.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/nvoc/euclidean_128.csv")
vectorfile='/Users/mengqizhou/Desktop/datamining/programing3/data/initialdata/weighted_vectors.csv'
vector = genfromtxt(vectorfile, dtype=float,delimiter = ',')   
vector = np.array(vector)
for metric in (0,1):
    for method in (0,1):
        vnocfile=[]
        nvocfile=[]
        if metric ==0:#cosine
            if method==0:#kmeans
                vnocfile=vkc
                nvocfile=nkc
            elif method==1: 
                vnocfile=vhc
                nvocfile=nhc
        elif metric==1:#euclidean
            if method==0:#kmeans
                vnocfile=vke
                nvocfile=nke
            elif method==1:#hierarchy
                vnocfile=vhe
                nvocfile=nhe
        for i in range(0,len(vnocfile)):
            vnoc=[]
            nvoc=[]
            with open(vnocfile[i],'rU') as f:
                reader = csv.reader(f)
                for row in reader:
                    vnoc.append(row)
            f.close()
            temps=[]
            for row in vnoc:
                temp=[]
                for value in row:
                    if value!='':
                        temp.append(value)
                temps.append(temp)
            vnoc=temps
            nvoc=genfromtxt(nvocfile[i], dtype=int,delimiter = ',')
            sd=[]
            total=0
            for value in nvoc:
                total+=value
            for cn in range(0,len(vnoc)):
                vectors=[]
                for value in vnoc[cn]:
                    vectors.append(vector[int(value)])
                vectors=np.array(vectors)
                sd.append(np.sum(np.std(vectors,axis=0)))          
            if metric==0 and method==0:print "cosine,kmeans"
            elif metric==0 and method==1:print "cosine, hierarchy"
            elif metric==1 and method==0: print "euclidean,kmeans"
            elif metric==1 and method==1: print "euclidean,hierarchy" 
            print str(len(vnoc))+"clusters,standard devidation= "+str(np.dot(sd,nvoc)/total)
