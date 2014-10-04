from leftover import lefttransaction
ltbase="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/14/lefttransaction3/"
nfbase="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/14/transactionswithoutfeature/"
rulebase="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/14/prunedrules3/"
tbase="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/14/lefttransaction2/"
for i in (0,11):
    lefttransaction(ltbase+str(i),nfbase+str(i),rulebase+str(i),tbase+str(i))