from prune import prune
from time import time
outputbase="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm1/output"
prbase="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm1/prunedrules"
start = time()
for i in range(1,5):
    prune(outputbase+str(i),prbase+str(i))
end=time()
print "total time: "+str(end-start)+" sec"