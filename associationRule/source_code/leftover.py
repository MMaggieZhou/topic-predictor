def lefttransaction(lefttransaction,t,rule,transaction):
    rule_file=open(rule,"r")
    lines=rule_file.readlines()
    rule_file.close()
    rules=[]
    for line in lines:
        rules.append(line.split())   
    training_transactions=open(transaction,"r")
    lines=training_transactions.readlines()
    transactions=[]
    for line in lines:
        transactions.append(line.split())
    
    lefttransactions=[]
    t1=[]
    for transaction in transactions:
        covered=0
        nofeature=1
        for word in transaction:
            if word[0]=='F':
                nofeature=0
        for rule in rules:
            coveredbytherule=1       
            for i in range(1,len(rule)-2):
                if rule[i] not in transaction:
                    coveredbytherule=0
                    break  
            if coveredbytherule==1:
                covered=1
                break
        if covered==0 and nofeature==0:
            lefttransactions.append(transaction)
        if nofeature==1:
            t1.append(transaction)
    f=open(lefttransaction,'w')
    for item in lefttransactions:
        f.write(" ".join(x for x in item)+"\n") 
    f=open(t,'w')
    for item in t1:
        f.write(" ".join(x for x in item)+"\n") 
    print "left transaction: "+str(len(lefttransactions))
    print "empty transaction: "+str(len(t1))
    print "total transaction: "+str(len(transactions))