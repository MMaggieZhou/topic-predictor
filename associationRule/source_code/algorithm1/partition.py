import csv
from numpy import genfromtxt
tan="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/test_article_numbers.csv"#test article number
test=genfromtxt(tan,dtype=int,delimiter=',')
tran="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/training_article_numbers.csv"#training article number
training=genfromtxt(tran,dtype=int,delimiter=',')
allvector="/Users/mengqizhou/Desktop/datamining/assignment5/feature_vectors.csv"
alllabel="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/binary_class_labels.csv"
folder="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm1/"
vectors=[]
with open (allvector,'rU') as f:
    reader=csv.reader(f)
    for row in reader:
        vectors.append(row)
f.close()
labels=[]
with open (alllabel,'rU') as f:
    reader=csv.reader(f)
    for row in reader:
        labels.append(row)
f.close()
tevs=[]#test vectors
tels=[]#test labels
trvs=[]#training vectors
trls=[]#training labels
for i in range(0,len(vectors)):
    if i in test:
        tevs.append(vectors[i])
        tels.append(labels[i])
    elif i in training:
        trvs.append(vectors[i])
        trls.append(labels[i]) 
with open(folder+"test_vectors.csv", 'wb') as f:
        writer = csv.writer(f)
        for item in tevs:
            writer.writerow(item)
f.close
with open(folder+"test_labels.csv", 'wb') as f:
    writer = csv.writer(f)
    for item in tels:
        writer.writerow(item)
f.close
with open(folder+"training_vectors.csv", 'wb') as f:
    writer = csv.writer(f)
    for item in trvs:
        writer.writerow(item)
f.close
with open(folder+"training_labels.csv", 'wb') as f:
    writer = csv.writer(f)
    for item in trls:
        writer.writerow(item)
f.close
len=0
for item in vectors[0]:
    if item!='':
        len+=1
    else: break
print "number of features: "+str(len)
len=0
for item in vectors[2]:
    if item!='':
        len+=1
    else: break
print "number of features: "+str(len)