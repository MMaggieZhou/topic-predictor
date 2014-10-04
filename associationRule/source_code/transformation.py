import csv
def transform(stvf,stlf,tf):
    stv=[]#sample training vectors
    stl=[]#sample training labels
    with open (stvf,'rU') as f:
        reader=csv.reader(f)
        for row in reader:
            stv.append(row)
    f.close()
    with open (stlf,'rU') as f:
        reader=csv.reader(f)
        for row in reader:
            stl.append(row)
    f.close()
    transaction=[]
    nv = len(stv) #number of vectors
    nl = len(stl)#number of label vectors
    if (nv!=nl):
        print "error!"
    for i in range(0,nv):
        temp=[]
        for j in range (0,4953):
            if (stv[i][j]==str(1)):
                if j<10:
                    temp.append("F00"+str(j))
                elif j<100:
                    temp.append("F0"+str(j))
                else:
                    temp.append("F"+str(j))
        for k in range(0,119):
            if (stl[i][k]==str(1)):
                if k<10:
                    temp.append("L00"+str(k))
                elif k<100:
                    temp.append("L0"+str(k))
                else:
                    temp.append("L"+str(k))
        #print temp
        transaction.append(temp)
    #print len(transaction)
    f=open(tf,'w')
    for row in transaction:
        f.write(" ".join(x for x in row)+"\n")