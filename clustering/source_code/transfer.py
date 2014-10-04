from numpy import genfromtxt
import numpy as np
import csv

file1 = []
file1.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy_label/cosine_4.csv")
file1.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy_label/cosine_8.csv")
file1.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy_label/cosine_16.csv")
file1.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy_label/cosine_32.csv")
file1.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy_label/cosine_64.csv")
file1.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy_label/cosine_128.csv")
file2=[]
file2.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy_label/euclidean_4.csv")
file2.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy_label/euclidean_8.csv")
file2.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy_label/euclidean_16.csv")
file2.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy_label/euclidean_32.csv")
file2.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy_label/euclidean_64.csv")
file2.append("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy_label/euclidean_128.csv")
for iteration in range(0,2):
    if iteration==0:file=file1
    elif iteration==1:file=file2
    for item in file:
        labels = genfromtxt(item, dtype=int,delimiter = ',')
        labels = np.array(labels)
        dict = {}
        for i in range(0,len(labels)):#vector number
            c = labels[i]
            if (dict.has_key(c)==False):
                dict[c]=[]
                dict[c].append(i)
            else: dict[c].append(i)
        
        vnoc = dict.values()
        print len(vnoc)
        nvoc=[]
        for item in vnoc:
            nvoc.append(len(item))
        #with open("/Users/mengqizhou/Desktop/datamining/programing3/data/vnoc/sample_euclidean_"+str(len(vnoc))+".csv", 'wb') as f:
        if iteration==0:
            with open("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/vnoc/cosine_"+str(len(vnoc))+".csv", 'wb') as f:
                    writer=csv.writer(f)
                    for item in vnoc:
                        writer.writerow(item)
            f.close()
            np.savetxt("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/nvoc/cosine_"+str(len(nvoc))+".csv", nvoc,'%i',delimiter=",")
        elif iteration==1:
            with open("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/vnoc/euclidean_"+str(len(vnoc))+".csv", 'wb') as f:
                writer=csv.writer(f)
                for item in vnoc:
                    writer.writerow(item)
            f.close()
            np.savetxt("/Users/mengqizhou/Desktop/datamining/programing3/data/hierarchy/nvoc/euclidean_"+str(len(nvoc))+".csv", nvoc,'%i',delimiter=",")