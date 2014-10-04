from time import time
from distance_marics import cosine
from distance_marics import euclidean
import math
import numpy as np


def clustering(vector,seed,similarity):#vector and seed needs to be numpy array,float, similarity is a string
    threshold = 0
    if (similarity =='cosine'): threshold = 0.0001
    elif (similarity=='euclidean'): threshold = 0.01
    nvoc = []#number of vectors in each cluster, integer
    #average of clusters, for convergence test, float
    iteration=0
    l = len(seed)
    mean = [None]*l
    vnoc = [None]*l
    nvoc = [0]*l
    temp = []
    converged = False
    while (converged ==False and iteration<20):
        iteration+=1
        converged = True  
        t1 = time()
        #for every item in the feature_vectors 
        vn=0#vector number
        for row in vector: 
            ss = 0 #maximum similarity
            i=[]#seed number 
            j=0      
            for item in seed:
                if (similarity == "cosine"):
                    Similarity = cosine.cosine_similarity(item, row)
                elif (similarity == "euclidean"):
                    Similarity = euclidean.euclidean_similarity(item, row)
                #print "similarity"
                #print similarity
                if (Similarity > ss):
                    ss = Similarity
                    i=[]
                    i.append(j)
                elif (Similarity == ss):
                    i.append(j)
                j+=1
            for iitem in i:
                nvoc[iitem]+=1
                #print nvoc
                #print vnoc[iitem]
                if(vnoc[iitem]==None):
                    vnoc[iitem]=[]
                    vnoc[iitem].append(vn)                   
                else: vnoc[iitem].append(vn) 
                #update the mean centroids
                if (mean[iitem] == None):
                    mean[iitem]=row
                else:
                    for p in range (0,len(mean[iitem])):
                        mean[iitem][p]=float(mean[iitem][p]*(nvoc[iitem]-1)+row[p])/nvoc[iitem]
            vn+=1
        #check convergence
        for i in range(0,len(seed)):
            if mean[i]==None:
                converged=False
                break
            for j in range(0,len(seed[0])):
                if (math.fabs(seed[i][j]-mean[i][j])>threshold):
                    converged = False
        print "iteration= "+str(iteration)+" ,time = "+str(time()-t1)+" seconds"
        if converged == True:
            print "converged"
            return mean,vnoc,nvoc
        #delete empty mean and vnoc, assume they won't be totally empty!
        tempvnoc = []
        tempMean = []
        tempnvoc=[]
        for i in range(0,len(vnoc)):
            if vnoc[i]!=None:
                tempvnoc.append(vnoc[i])
                tempMean.append(mean[i])
                tempnvoc.append(nvoc[i])
        vnoc=tempvnoc
        mean=tempMean
        nvoc=tempnvoc
        #delete redundant mean and vnoc
        tempvnoc = []
        tempMean = []
        tempvnoc.append(vnoc[0])     
        tempMean.append(mean[0])
        tempnvoc.append(nvoc[0])
        for i in range(1,len(vnoc)):
            Repeat = False
            for item in tempvnoc:
                repeat = True
                if (len(vnoc[i])!=len(item)):
                    repeat = False
                else:
                    for j in range(0,len(vnoc[i])):
                        if math.fabs(item[j]-vnoc[i][j])>0.001:
                            repeat = False
                            break
                if repeat ==True:
                    Repeat = True
                    break
            if Repeat==False:
                tempvnoc.append(vnoc[i])
                tempMean.append(mean[i]) 
                tempnvoc.append(nvoc[i])
                
        if converged ==False:
            seed = tempMean
            l = len(seed)
            mean = [None]*l
            vnoc = [None]*l
            nvoc = [0]*l
    print" not converged"
    return tempMean, tempvnoc,tempnvoc
