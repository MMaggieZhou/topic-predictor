import knn_classifier

main_folder = "/Users/mengqizhou/Desktop/datamining"
folder1 = "/Users/mengqizhou/Desktop/datamining/datasplit_by_3_fold"
folder2 = "/Users/mengqizhou/Desktop/datamining/datasplit_by_5fold"
address = []
address.append(folder1)
address.append(folder2)
num_class = 119
num_feature = 456
sampling_fold = 10
K=30

for folder in address:
    knn_classifier.classify(folder, main_folder, num_class, num_feature, sampling_fold, K)