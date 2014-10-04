import csv
def calculate_accuracy(tl, stlf):
    test_labels=open(tl,"r")
    lines=test_labels.readlines()
    test_labels.close()
    labels=[]
    for line in lines:
        labels.append(line.split())
    known_labels=[]
    stl=[]
    with open (stlf,'rU') as f:
        reader=csv.reader(f)
        for row in reader:
            stl.append(row)
    f.close()
    if len(labels)!=len(stl): print "error"
    for i in range(0,len(stl)):
        temp=[]
        for k in range(0,119):
            if (stl[i][k]==str(1)):
                if k<10:
                    temp.append("L00"+str(k))
                elif k<100:
                    temp.append("L0"+str(k))
                else:
                    temp.append("L"+str(k))
        known_labels.append(temp)
    sum=0
    for i in range(0,len(labels)):
        n=0
        for label in labels[i]:
            if label in known_labels[i]:
                n+=1
        #sum+=(float(n*n)/len(labels[i])/len(known_labels[i]))
        sum+=(float(n)/float(len(labels[i])))
    if len(labels)!=0:
        return sum/len(labels), len(labels)
    else:
         return 0.0,0

