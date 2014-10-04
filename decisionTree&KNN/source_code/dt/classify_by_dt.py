from __future__ import print_function 
import DecisionTree
import csv
import time


main_folder = "/Users/mengqizhou/Desktop/datamining"
folder1 = "/Users/mengqizhou/Desktop/datamining/datasplit_by_3_fold"
folder2 = "/Users/mengqizhou/Desktop/datamining/datasplit_by_5fold"
address = []
address.append(folder1)
address.append(folder2)
num_class = 119
num_feature = 456
#num_article = 8391

for folder in address:
    feature_num_class = []
    result = open(folder+"/results.txt","w")
    #training_data = []

    with open(main_folder+"/feature_num_of_classes.csv", 'rU') as f:
        reader=csv.reader(f)
        for row in reader:
            feature_num_class.append(row)
    f.close()
    
    #with open(folder+"decision_tree_training_dataset.csv",'rb') as f:
       # reader = csv.reader(f)
        #for row in reader:
            #training_data.append(row)
    #f.close()
    start_time = time.time()
    root_nodes = []
    decision_trees =[]
    file=folder+"/decision_tree_training_dataset.csv"
    for i in range(0,num_class):
        feature_num = []
        for number in feature_num_class[i]:
            if number == '':
                break
            feature_num.append(int(number)+1)
        dt = DecisionTree.DecisionTree( training_datafile = file,
                                csv_class_column_index = (1+num_feature+i),
                                csv_columns_for_features = feature_num,
                                entropy_threshold = 1,
                                max_depth_desired = 100,
                                symbolic_to_numeric_cardinality_threshold = 10,
                              )
        dt.get_training_data()
        dt.calculate_first_order_probabilities()
        dt.calculate_class_priors()
        root_node = dt.construct_decision_tree_classifier()
        decision_trees.append(dt)
        root_nodes.append(root_node)
    modeling_time = time.time()-start_time
    
    print("modeling_time = ",modeling_time," s", file = result)
    print("number of decision tree created = ", len(decision_trees), file = result)
    #print modeling_time
       
    test_data = []
    features = []
    with open(main_folder +"/features_after_trim.csv", 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            features.append(row)
    f.close()
    
    with open(folder + "/test_feature_vectors.csv", 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            test_data.append(row)
    f.close()
    
    start_time = time.time()
    i = 0
    with open(folder+"/classified_binary_labels.csv",'wb') as f:
        writer = csv.writer(f)
        for article_feature in test_data:
            binary_labels = []

            for j in range(0,num_class):#feature_numbers in feature_num_class:
                data = []
                for number in feature_num_class[j]:
                    if number=='':
                        break
                    data.append(features[0][int(number)]+" = "+article_feature[int(number)])
                
                prob_hash = decision_trees[j].classify(root_nodes[j],data)
                for item in prob_hash:
                    if (item is not 'solution_path') and (prob_hash[item] >=0.5):
                        binary_label = item[-1:]
                        break
                #print ("test = : ", (binary_label),file = result )
                binary_labels.append(binary_label)
            #print ("article number = ", i, " labels: ", binary_label, file = result)
            writer.writerow(binary_labels)
            i+=1
        f.close()
    classifying_time = time.time()-start_time
    print("classifying_time = ",classifying_time," s", file = result)

    true_binary_labels = []
    classified_binary_labels = []
    
    with open(folder+"/training_binary_class_labels.csv", 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            true_binary_labels.append(row)
    f.close()
    
    with open(folder+"/classified_binary_labels.csv", 'rb') as f:
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

    
    