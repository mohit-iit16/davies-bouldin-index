import pandas as pd
import numpy as np
from sklearn.cluster import k_means
from scipy.spatial import distance
from numpy import linalg as LA
from scipy.linalg import norm

n=10
clf=k_means(X4, n_clusters=n)
centroids=clf[0]
labels=clf[1]
nc=len(centroids)

def cluster_scatter(centroid,i):
    index=0
    S_i=0
    for a in range(len(X4new)) :
        if labels[a]==i:
            dst = dist = np.linalg.norm(centroid-(X4new[a]))
            S_i+=dst
    #print S_i       
    c=norm(centroid)
    #print 'c',c
    Si=S_i/c
    #print 'SI',Si
    return Si
    
scat=np.zeros((10,1))
for i in range(10):
    scat[i]=cluster_scatter(centroids[i],i)
    
def distance_clusters(a,b):
    d_i_j=np.linalg.norm(a-b)
    
    return d_i_j
    
def R_i_j(centroids,X4new):
    X_syn= np.zeros((90,1))
    p=0
    q=0
    for i in range(len(centroids)):
        for j in range(len(centroids)):
            if i!=j:
                #print'scat1',scat[i],'scat2', scat[j]
                dij=distance_clusters(centroids[i],centroids[j])
                #print 'dij', dij
                X_syn[p] =(scat[i]+scat[j])/dij
                #print 'Xin', X_syn[p]
                p+=1
            else:
                    continue
                    
    return X_syn
    
def R_i(x):
    c=len(x)
    index=0
    R_n=np.zeros(((c/9),1))
    for i in range(0,c,9):
        temp=x[i:i+9]
        R_n[index]=np.max(temp)
        index+=1        
        
    return R_n
    
def db(z):
    D=0
    for i in y:
        D+=i
    db=D/nc
    return db