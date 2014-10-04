from transformation import transform
trvb="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/14/binary/training_vectors_"#training vector base
trlb="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/14/binary/training_labels_"#training label base
ttb="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/14/transactions/training_transactions_"#training trainsactions base
tevb="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/14/binary/test_vectors_"
telb="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/14/binary/test_labels_"
tetb="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm2/14/transactions/test_transactions_"
for i in range(0,14):
    transform(tevb+str(i)+".csv",telb+str(i)+".csv", tetb+str(i))