import csv

def partition_articles(folder,K_fold,number_of_article):
    K= K_fold
    ExistenceVector = []
    article_number=[]
    binary_class_labels=[]
    Attributes = []
    class_dict = []
    for i in range(0,number_of_article):
        article_number.append(i)
    with open(folder+"/feature_vectors_trim.csv", 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            ExistenceVector.append(row)
        f.close()
        
    with open(folder+"/binary_class_labels.csv", 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            binary_class_labels.append(row)
        f.close()
        
    if False: from random import shuffle; X=list(article_number); shuffle(article_number)
    for k in xrange(K):
        training = [x for i, x in enumerate(article_number) if i % K != k]
        validation = [x for i, x in enumerate(article_number) if i % K == k]
    #return training,validation
        
    """************obtain_training_data********** """       
#def get_training_data(folder,article_Class,binary_class_labels,training,ExistenceVector):    
    training_ClassColumn = []#filter the empty labels from binary_class_labels
    training_VectorColumn = []#filter the unuseful vectors
    training_ArticleColumn = []#article numbers
    
    
    for i in training:  
        training_ClassColumn.append(binary_class_labels[i])
        training_VectorColumn.append(ExistenceVector[i])
        training_ArticleColumn.append(i)
    #return training_ClassColumn,training_VectorColumn,training_ArticleColumn
    with open(folder+"/training_binary_class_labels.csv", 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(training_ClassColumn)
    f.close
    with open(folder+"/training_feature_vectors.csv", 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(training_VectorColumn)
    f.close
    with open(folder+"/training_article_numbers.csv", 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(training_ArticleColumn)
    f.close
    """************test_data********** """
#def get_test_data(articleClass,binary_class_labels,validation,ExistenceVector):    
    validation_ClassColumn = []
    validation_VectorColumn = []
    validation_ArticleColumn = []
    
    for i in validation:
        validation_ClassColumn.append(binary_class_labels[i])
        validation_VectorColumn.append(ExistenceVector[i])
        validation_ArticleColumn.append(i)
    
    #return validation_ClassColumn,validation_VectorColumn,validation_ArticleColumn
    with open(folder+"/test_binary_class_labels.csv", 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(validation_ClassColumn)
    f.close
    with open(folder+"/test_feature_vectors.csv", 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(validation_VectorColumn)
    f.close
    with open(folder+"/test_article_numbers.csv", 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(validation_ArticleColumn)
    f.close
     

    training_data = [] #"""************the data to put into training.csv**********"""    
    temp = []
    with open(folder+"/unique_classes.csv", 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            class_dict.append(row)
    with open(folder+"/features_after_trim.csv", 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            Attributes.append(row)
        f.close()
    
    temp.append("")
    for attribute in Attributes[0]:
        temp.append(attribute)
    for item in class_dict[0]:
        temp.append(item)
    #print len(temp)    
    training_data.append(temp)
      
    i=0
    for article in training_ArticleColumn:
        temp = []
        temp.append(article)
        for bool in training_VectorColumn[i]:
            temp.append(bool)
        for each in training_ClassColumn[i]:
            temp.append(each)    
        training_data.append(temp)
        i+=1
    #print len(temp)
    """************the data to put into test.csv**********"""   
    validation_data = []
    temp = []
    
    temp.append("")
    for attribute in Attributes[0]:
        temp.append(attribute)
    for item in class_dict[0]:
        temp.append(item)
    validation_data.append(temp)
    #print len(temp)
    i=0
    for article in validation_ArticleColumn:
        temp = []
        temp.append(article)
        for bool in validation_VectorColumn[i]:
            temp.append(bool)
        for each in validation_ClassColumn[i]:
            temp.append(each)
        validation_data.append(temp)
        i+=1
    
    #print len(temp)
    """*****************write into csv************************"""
    #training_file = '/Users/mengqizhou/Desktop/datamining/assignment2/training.csv'
    with open(folder+"/decision_tree_training_dataset.csv", 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(training_data)
    f.close
    #test_file = '/Users/mengqizhou/Desktop/datamining/assignment2/test.csv'
    with open(folder+"/decision_tree_test_dataset.csv", 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(validation_data)
    f.close
    """
    if (training_data[0][0]!=""):
        print training_data[0][0]
        print "there is a program"
    """

