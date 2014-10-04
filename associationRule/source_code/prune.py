from math import fabs
def prune(rf,newrule_file):
    rule_file = open(rf,"r")
    lines=rule_file.readlines()
    rule_file.close()
    rules=[]
    therules=[]
    for line in lines:
        temprule=[]
        templabel=[]
        tempfeature=[]
        tempquantity=[]
        satisfy =1
        rule = line.split()
        label=rule[0]
        if (label[0])=='F':
            satisfy=0
        else: templabel.append(rule[0])
        feature= []
        for j in range(2,len(rule)-2):
            if (rule[j][0])=='L':
                satisfy=0 
            else: tempfeature.append(rule[j])
        tempquantity.append(rule[len(rule)-2].replace('(','').replace(',',''))
        tempquantity.append(rule[len(rule)-1].replace(')',''))
        if satisfy==1:
            temprule.append(templabel)
            temprule.append(tempfeature)
            temprule.append(tempquantity)     
            rules.append(temprule) 
    #prune subsumed rules
    for i in range(0,len(rules)):
        redundant=0
        for j in range(0,len(rules)):
            if i!=j:
                belongs=1
                for feature in rules[i][1]:#if every feature is in another rule
                    if feature not in rules[j][1]:
                        belongs=0
                        break
                samelabel=0
                if rules[i][0]==rules[j][0]:samelabel=1
                if (belongs==1 and samelabel==1):
                    if (fabs(float(rules[i][2][0])-float(rules[j][2][0]))<0.001):
                        if (fabs(float(rules[i][2][1])-float(rules[j][2][1]))<1):
                            redundant=1
                            break
                contains=1
                for feature in rules[j][1]:
                    if feature not in rules[i][1]:
                        contains=0
                        break
                if (contains==1 and samelabel==1):
                    if (-float(rules[i][2][1])+float(rules[j][2][1])>1):
                        redundant=1
                        break
        if redundant==0:therules.append(rules[i])
    f=open(newrule_file,'w')
    for rule in therules:
        temp=rule[0]+rule[1]+rule[2]
        f.write(" ".join(x for x in temp)+"\n")   
    print len(therules)           
                