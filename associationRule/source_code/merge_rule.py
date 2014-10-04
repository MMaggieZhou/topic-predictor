oldsize=3024
newsize=442
combined_rule="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/14/combinedrules/11"
new_rule="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/14/prunedrules3/11"
old_rule="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/14/combinedrules/11"
oldrules=[]
dest=open(old_rule,"r")
lines=dest.readlines()
dest.close()
for line in lines:
    oldrules.append(line.split())
print len(oldrules)    
newrules=[]
new=open(new_rule,"r")
lines=new.readlines()
new.close()
for line in lines:
    newrules.append(line.split())
print len(newrules)
for rule in newrules:
    rule[len(rule)-2]= str(float(rule[len(rule)-2])*newsize/oldsize)
    oldrules.append(rule)
print len(oldrules)
f=open(combined_rule,'w')
for item in oldrules:
    f.write(" ".join(x for x in item)+"\n") 
