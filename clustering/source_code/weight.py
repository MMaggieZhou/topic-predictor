from numpy import genfromtxt
import numpy as np

vector_file = "/Users/mengqizhou/Desktop/datamining/programing3/data/initialdata/feature_vectors.csv"
weight_file = '/Users/mengqizhou/Desktop/datamining/programing3/data/initialdata/weight.csv'
weighted_vector = '/Users/mengqizhou/Desktop/datamining/programing3/data/initialdata/weighted_vectors.csv'
sample_file = '/Users/mengqizhou/Desktop/datamining/programing3/data/initialdata/sample_feature_vectors.csv'
weighted_sample = '/Users/mengqizhou/Desktop/datamining/programing3/data/initialdata/weighted_sample.csv'

'''
for i in range(0,l):
    count.append(0)
for vector in vectors:
    for j in range(0, l):
        if vector[j]==1:
            count[j]+=1
weight = []
for i in range(0,l):
    weight.append(float(691)/math.sqrt(float(count[i]))

print weight
np.savetxt(weight_file, weight, '%5.2f',delimiter=",") 
'''
vectors = genfromtxt(sample_file, dtype=float,delimiter = ',')
vectors = np.array(vectors)
weights =genfromtxt(weight_file, dtype=float,delimiter = ',')
weights = np.array(weights)
'''
weight = []
for item in weights:
    weight.append(math.sqrt(float(item)))
'''
new = np.multiply(vectors, weights)
print len(new), len(new[0])
np.savetxt(weighted_sample, new, '%5.2f',delimiter=",") 
