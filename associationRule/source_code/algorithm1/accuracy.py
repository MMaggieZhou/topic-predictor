from accuracy2 import calculate_accuracy

tlbase="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm1/test_labels"
blbase="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm1/test_labels.csv"
accuracy,len=calculate_accuracy(tlbase,blbase)
print "accuracy= "+str(accuracy) 
