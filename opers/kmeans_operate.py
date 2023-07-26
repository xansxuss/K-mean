import os,cv2
import numpy as np

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def op_k_means(img):
    clt = KMeans(n_clusters=3,random_state=42).fit(img)

    centers = clt.cluster_centers_
    
    new = []
    for x in range(len(centers)):
        new.append(list(centers[x]/255))
    
    labels = np.bincount(clt.labels_ ) 
    labels = labels / len(clt.labels_)

    out_center=[]
    out_label =[]
    res_labels = list(reversed(np.argsort(labels)))
    for i in res_labels:
        out_center.append(new[i])
        out_label.append(labels[i])
    
    return out_center, out_label