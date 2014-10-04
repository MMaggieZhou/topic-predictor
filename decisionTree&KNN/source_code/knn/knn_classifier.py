from __future__ import print_function 
import csv
import time
import KNNClassifier
import random


#num_article = 8391
def classify(folder, main_folder,num_class, num_feature,F, K):
#for folder in address: 
    feature_num_class = []
    with open(main_folder+"/feature_num_of_classes.csv",'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            feature_num_class.append(row)
    f.close()
    
    binary_class_labels = []
    with open(main_folder+"/binary_class_labels.csv",'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            binary_class_labels.append(row)
    f.close()
    
    feature_vectors = []
    with open(main_folder+"/feature_vectors_trim.csv",'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            feature_vectors.append(row)
    f.close()
    
    result = open(folder+"/knn_results.txt","w")
    class_frequency = []
    feature_weights = []
    training_article_nums = []
    test_article_nums = []
    sample_training_article_nums = []
    sample_test_article_nums = []
    sample_training_vectors = []
    sample_training_labels = []
    sample_test_vectors = []
    sample_test_labels = []
    
    with open(folder+"/training_article_numbers.csv", 'rb') as f:
        reader=csv.reader(f)
        for row in reader:
            training_article_nums.append(row)
    f.close()
    
    with open(folder+"/test_article_numbers.csv", 'rb') as f:
        reader=csv.reader(f)
        for row in reader:
            test_article_nums.append(row)
    f.close()    

    with open(main_folder+"/class_frequency.csv", 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            class_frequency.append(row)
    f.close()
    with open(main_folder+"/weight_feature_class.csv", 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            feature_weights.append(row)
    f.close() 
    
    if False: from random import shuffle; X=list(training_article_nums[0]); shuffle(training_article_nums[0])
    for k in xrange(F):
        #sample_training = [x for i, x in enumerate(article_number) if i % K != k]
        sample_training = [x for i, x in enumerate(training_article_nums[0]) if i % F == k]
    with open(folder+"/sample_training_article_num.csv", 'wb') as f:
        writer=csv.writer(f)
        writer.writerow(sample_training)
    f.close()
    
    if False: from random import shuffle; X=list(test_article_nums[0]); shuffle(test_article_nums[0])
    for k in xrange(F):
        #sample_training = [x for i, x in enumerate(article_number) if i % K != k]
        sample_test = [x for i, x in enumerate(test_article_nums[0]) if i % F == k]
    with open(folder+"/sample_test_article_num.csv", 'wb') as f:
        writer=csv.writer(f)
        writer.writerow(sample_test)
    f.close()
    
    with open(folder+"/sample_training_article_num.csv", 'wb') as f:
        writer=csv.writer(f)
        writer.writerow(sample_training)
    f.close()
    
    with open(folder+"/sample_training_vectors.csv", 'wb') as f:
        writer=csv.writer(f)
        for item in sample_training:
            sample_training_vectors.append(feature_vectors[int(item)])
            writer.writerow(feature_vectors[int(item)])
    f.close() 
    
    with open(folder+"/sample_training_labels.csv", 'wb') as f:
        writer=csv.writer(f)
        for item in sample_training:
            sample_training_labels.append(binary_class_labels[int(item)])
            writer.writerow(binary_class_labels[int(item)])
    f.close()
    
    with open(folder+"/sample_test_vectors.csv", 'wb') as f:
        writer=csv.writer(f)
        for item in sample_test:
            sample_test_vectors.append(feature_vectors[int(item)])
            writer.writerow(feature_vectors[int(item)])
    f.close() 
    
    with open(folder+"/sample_test_labels.csv", 'wb') as f:
        writer=csv.writer(f)
        for item in sample_test:
            sample_test_labels.append(binary_class_labels[int(item)])
            writer.writerow(binary_class_labels[int(item)])
    f.close()
    modeling_time = 0
    classifying_time=0
    inversed_classified_labels = []

    for i in range(0,num_class):
        temp = []
        feature_num = feature_num_class[i]
        the_class_frequency = class_frequency[0][i]
        start_time = time.time()
        class_column = []
        for item in sample_training_labels :
            if item[0]=='':
                break
            class_column.append(item[i])
             
        knn=KNNClassifier.train(sample_training_vectors, class_column, K, typecode=None)
        modeling_time+=(time.time()-start_time)
        #print "modeling time = ", modeling_time, "s"
        #print "classifier number = ",i+1       
        for article in sample_test_vectors:
            start_time = time.time()
            if article[0]=='':
                break            
            label = KNNClassifier.classify(knn, article,feature_num, the_class_frequency,None , feature_weights[0])
            classifying_time += (time.time()-start_time)
            #print "classifying time = ", classifying_time,"s"
            #print "class number = ",i," label = ", label
            temp.append(label)
        print( i+1,"out of ",num_class," has been classified") 
        inversed_classified_labels.append(temp)  
    print("modeling time = ", modeling_time,"s", file = result)
    print("number of knn classifiers = ", num_class, file = result)
    print("classifying time = ", classifying_time, "s", file = result)
    #inverse-the inversed label matrix
    num_article = len(inversed_classified_labels[0])
    print("calssified article number = ", num_article, file = result)
    with open(folder+"/knn_classified_sample_labels.csv", 'wb') as f:
        writer = csv.writer(f)
        for i in range(0,num_article):
            temp = []
            for j in range(0,num_class):
                temp.append(inversed_classified_labels[j][i])
            writer.writerow(temp)
    f.close()
    calculate_accuracy()
    
def calculate_accuracy(folder, num_class,result):    
    true_binary_labels = []
    classified_binary_labels = []
    
    with open(folder+"/sample_test_labels.csv", 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            true_binary_labels.append(row)
    f.close()
    
    with open(folder+"/knn_classified_sample_labels.csv", 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            classified_binary_labels.append(row)
    f.close()  
    
          
    total = 0
    correct = 0
    num_article = len(classified_binary_labels)
    for i in range(0,num_article):
        if classified_binary_labels[i][0]=='':
            break
        for j in range(0,num_class):
            total += 1
            if (classified_binary_labels[i][j]==true_binary_labels[i][j]):
                correct +=1
    accuracy = float (correct)/total 
    print("accuracy = ",accuracy, file = result)