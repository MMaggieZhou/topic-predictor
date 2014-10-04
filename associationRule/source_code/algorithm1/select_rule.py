from select_rules import select_rules
from time import time
tlbase="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm1/test_labels"
ttbase="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm1/test_transactions"
rbase="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm1/combined_rules"
dls=['F015','F016']
start=time()
select_rules(tlbase,ttbase,rbase,dls)
end=time()
print "time for classification: "+str(end-start)+" sec"