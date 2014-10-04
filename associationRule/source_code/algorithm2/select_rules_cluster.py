from select_rules import select_rules
from time import time
tlbase="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/8/test_labels/"
ttbase="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/8/transactions/test_transactions_"
rbase="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/8/combinedrules/"

dlbase=open("/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/8/default_labels/default_labels","r")
dls=[]
lines=dlbase.readlines()
for line in lines:
    dls.append(line.split())
start=time()
for cluster in range(0,8):
    select_rules(tlbase+str(cluster),ttbase+str(cluster),rbase+str(cluster),dls[cluster])
end=time()
print "total time: "+str(end-start)+" sec"
