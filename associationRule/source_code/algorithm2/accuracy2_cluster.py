from numpy import genfromtxt
from accuracy2 import calculate_accuracy
import csv
tlbase="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/14/test_labels/"
blbase="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/14/binary/test_labels_"

sumacc=0.0
nv=[]
accuracy=[]
tvn=0
for cluster in range(0,14):
    temp1,temp2=calculate_accuracy(tlbase+str(cluster),blbase+str(cluster)+".csv")
    accuracy.append(temp1)
    nv.append(temp2)
    tvn+=nv[cluster]
    
for cluster in range(0,14):
    sumacc+=accuracy[cluster]*nv[cluster]/tvn
    print "cluster "+str(cluster)+": "+str(accuracy[cluster])
print "overall accuracy= "+str(sumacc) 
