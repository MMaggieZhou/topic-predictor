import math

def cosine_similarity(a,b):
    l=0;m=0; n=0;
    for i in range(0,len(a)):
        l += a[i]*b[i]
        m += a[i]*a[i]
        n += b[i]*b[i]
    return float(l)/math.sqrt(float(n*m))