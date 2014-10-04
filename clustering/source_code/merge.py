import numpy as np
import math
from distance_marics import cosine
from distance_marics import euclidean
import csv

def merge(vnoc, mean, nvoc, target,similarity,vector):
    noc=len(mean)
    while (noc>target):
        list = []
        max_sim=-1000.00
        for cn in range(0,noc):#cluster number
            for cn1 in range(cn+1,noc):
                if similarity=='cosine':
                    Similarity=cosine.cosine_similarity(mean[cn], mean[cn1])
                elif similarity=='euclidean':
                    Similarity=euclidean.euclidean_similarity(mean[cn], mean[cn1])              
                if Similarity==max_sim:
                    if cn in list :
                        list.append(cn1)
                    elif cn1 in list:
                        list.append(cn)
                elif Similarity>max_sim:
                        list.append(cn)
                        list.append(cn1)
                        max_sim=Similarity
        new_vnoc = vnoc[list[0]]
        for i in range(1,len(list)):
            new_vnoc+=vnoc[i]
        list1=[]
        for item in new_vnoc:
            if item not in list1:
                list1.append(item)
        list1=np.array(list1)
        new_vnoc=sorted(list1,key=int)
        new_nvoc=len(new_vnoc)
        vectors = []
        for vectornumber in new_vnoc:
            vectors.append(vector[vectornumber])
        vectors=np.array(vectors)
        new_mean=vectors.mean(axis=0)
        temp_vnoc = []
        temp_nvoc=[]
        temp_mean=[]
        for i in range(0,noc):
            if i not in list:
                temp_vnoc.append(vnoc[i])
                temp_nvoc.append(nvoc[i])
                temp_mean.append(mean[i])
            elif i ==list[0]:
                temp_vnoc.append(new_vnoc)
                temp_nvoc.append(new_nvoc)
                temp_mean.append(new_mean)
        vnoc=temp_vnoc
        nvoc=temp_nvoc
        mean=temp_mean
        noc-=(len(list)-1)
        nvoc = np.array(nvoc)
        mean = np.array(mean)
        if similarity=='cosine':
            print len(vnoc), len(nvoc),len(mean)
            np.savetxt("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/nvoc/cosine_"+str(len(nvoc))+".csv", nvoc, '%i',delimiter=",")
            np.savetxt("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/centroid/cosine_"+str(len(mean))+".csv", mean, '%5.2f',delimiter=",")
            with open("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/vnoc/cosine_"+str(len(vnoc))+".csv", 'wb') as f:
                writer=csv.writer(f)
                for item in vnoc:
                    writer.writerow(item)
            f.close()
        elif similarity=='euclidean':
            print len(vnoc), len(nvoc),len(mean)
            np.savetxt("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/nvoc/euclidean_"+str(len(nvoc))+".csv", nvoc, '%i',delimiter=",")
            np.savetxt("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/centroid/euclidean_"+str(len(mean))+".csv", mean, '%5.2f',delimiter=",")
            with open("/Users/mengqizhou/Desktop/datamining/programing3/data/kmeans/vnoc/euclidean_"+str(len(vnoc))+".csv", 'wb') as f:
                writer=csv.writer(f)
                for item in vnoc:
                    writer.writerow(item)
            f.close()
            