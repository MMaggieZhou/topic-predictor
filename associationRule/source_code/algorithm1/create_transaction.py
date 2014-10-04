from transformation import transform
trvb="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm1/training_vectors.csv"#training vector base
trlb="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm1/training_labels.csv"#training label base
ttb="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm1/training_transactions"#training trainsactions base
tevb="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm1/test_vectors.csv"
telb="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm1/test_labels.csv"
tetb="/Users/mengqizhou/Desktop/datamining/assignment5/algorithm1/test_transactions"

transform(tevb,telb, tetb)
transform(trvb,trlb, ttb)