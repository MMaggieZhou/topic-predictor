from numpy import genfromtxt
import csv
clusterinfo="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/14/cosine_14.csv"#vnoc
tan="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/test_article_numbers.csv"#test article number
tran="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/training_article_numbers.csv"#training article number
allvector="/Users/mengqizhou/Desktop/datamining/assignment5/feature_vectors.csv"
alllabel="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/binary_class_labels.csv"
folder="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/14/"

vnoc=[]
with open(clusterinfo,'rU') as f:
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

test=genfromtxt(tan,dtype=int,delimiter=',')
#test=np.array(vnoc)

training=genfromtxt(tran,dtype=int,delimiter=',')
#training=np.array(vnoc)

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

#figure out for the training data, which cluster it is in
#output:training_vector_1,2,3...8; training_label_1,2,...8
#output: test_vector_1,2,3...; training_label_1,2,...8

for i in range(0,len(vnoc)):
    tevs=[]#test vectors
    tels=[]#test labels
    trvs=[]#training vectors
    trls=[]#training labels
    for n in vnoc[i]:
        num=int(n)
        if num in test:
            tevs.append(vectors[num])
            tels.append(labels[num])
        elif num in training:
            trvs.append(vectors[num])
            trls.append(labels[num])    
    with open(folder+"test_vectors_"+str(i)+".csv", 'wb') as f:
        writer = csv.writer(f)
        for item in tevs:
            writer.writerow(item)
    f.close
    with open(folder+"test_labels_"+str(i)+".csv", 'wb') as f:
        writer = csv.writer(f)
        for item in tels:
            writer.writerow(item)
    f.close
    with open(folder+"training_vectors_"+str(i)+".csv", 'wb') as f:
        writer = csv.writer(f)
        for item in trvs:
            writer.writerow(item)
    f.close
    with open(folder+"training_labels_"+str(i)+".csv", 'wb') as f:
        writer = csv.writer(f)
        for item in trls:
            writer.writerow(item)
    f.close