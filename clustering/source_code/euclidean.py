import math
'''
Created on Nov 4, 2013

@author: mengqizhou
'''
#imput: two vectors
#output: value of their eucleadian distance

def euclidean_similarity(a,b):
    s = 0
    for i in range(0,len(a)):
        s += (a[i]-b[i])*(a[i]-b[i])
    return 400.00-math.sqrt(float(s))