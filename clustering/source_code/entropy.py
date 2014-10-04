import math
import numpy as np
from numpy import genfromtxt
import csv

    
def calculate_overall_entropy(vnoc, bcl,nvoc):
    total = 0
    for nv in nvoc:
        total+=nv
    entropys=[]#entropy of clusters, array
    oe =0 #overall entropy   
    l=len(vnoc)
    for k in range(0,l):#item is a array of a cluster
        fol = []#frequency of labels of the cluster,float
        for i in range(0,len(bcl[0])):#number of labels
            fol.append(float(0))#create an array recording the number of times that a label shows up, default is zero
        for number in vnoc[k]:#number is document number in a cluster array
            number=int(number)
            i = 0
            for j in range(0, len(bcl[number])):#label number
                if bcl[number][j] == 1: i+=1
            for j in range(0, len(bcl[number])):
                if bcl[number][j] == 1: 
                    fol[j]+= 1/float(i)
        entropy = calculate_entropy(fol,nvoc[k]) #calculate entropy based on the array recording the number of times that a label shows up
        entropys.append(entropy)

    #calculate overall entropy
    #test = 0
    for i in range(0,len(entropys)):
        oe = entropys[i]*nvoc[i]/total
    return oe

def calculate_entropy(appearance_class, number_of_document):
    entropy = 0.0
    #test = 0.0
    for item in appearance_class:
        #test+=item
        temp = item/float(number_of_document)
        if temp>0:
            entropy-=(temp*math.log(temp))
    #print number_of_document, test
    return entropy