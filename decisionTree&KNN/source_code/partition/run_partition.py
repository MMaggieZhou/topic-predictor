
import partition_dataset as pd
data_folder = "/Users/mengqizhou/Desktop/datamining"
output_folder1 = "/Users/mengqizhou/Desktop/datamining/3_fold"
output_folder2 = "/Users/mengqizhou/Desktop/datamining/5_fold"
K1= 3
k2 = 5
K = {}
K[K1]=output_folder1
K[K2]=output_folder2
number_of_articles = 8391

for k in K:
    pd.partition_articles(data_folder,K[K], k, number_of_articles)

