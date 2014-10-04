def select_rules(test_labels, test_transaction,combined_rule,default_label):
    test_transactions=open(test_transaction,"r")
    lines=test_transactions.readlines()
    transactions=[]
    for line in lines:
        transactions.append(line.split())
    combined_rules=open(combined_rule,"r")
    lines=combined_rules.readlines()
    rules=[]
    for line in lines:
        rules.append(line.split())
    alllabels=[]
    for transaction in transactions:
        labels=[]
        covered=0
        applied_rules=[]
        for j in range(0,len(rules)):
            #if every feature of rules are in transaction
            fit=1
            for k in range(1,len(rules[j])-2):
                if rules[j][k] not in transaction:
                    fit=0
                    break
            if fit==1:
                covered=1
                confidence=float(rules[j][len(rules[j])-1])
                support=float(rules[j][len(rules[j])-2])
                label=rules[j][0]
                applied_rules.append((confidence,support,label))
        if covered==0: 
            labels=default_label
        elif covered==1:
            applied_rules.sort(reverse=True)
            for i in range(0,5):
                if i < len(applied_rules):
                    if applied_rules[i][2] not in labels:
                        if applied_rules[i][0]>90 or i==0:
                            labels.append(applied_rules[i][2])
        alllabels.append(labels)
    print "number of rules: "+str(len(rules))
    f=open(test_labels,'w')
    for item in alllabels:
        f.write(" ".join(x for x in item)+"\n") 