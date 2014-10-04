from prune import prune
from time import time
outputbase="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/8/output1/"
prbase="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/8/prunedrules1/"
start=time()
for i in range(0,8):
    prune(outputbase+str(i),prbase+str(i))
end=time()
print (end-start)