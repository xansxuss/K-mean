import os, cv2,json
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.metrics.pairwise import pairwise_distances_argmin
from scipy.spatial import distance


import numpy as np
import argparse
from opers import img_open as imo
from opers import xml_operate as xo
from opers import file_operate as fo
from opers import kmeans_operate as kmeano


def parse_arguments() :
    parser = argparse.ArgumentParser(description="load data")
    parser.add_argument("--data_path",help="data path")
    parser.add_argument("--folder",help="multi folder",nargs='+')

    known_args, _ = parser.parse_known_args()
    return known_args

def get_label_img(img,axis):
    p1 = int(axis[0])
    p2 = int(axis[1])
    p3 = int(axis[2])
    p4 = int(axis[3])
    label_img = img[p2:p4, p1:p3]
    return label_img

def get_pixel_img(img,axis):
    p1 = int(axis[0])
    p2 = int(axis[1])
    p3 = int(axis[2])
    p4 = int(axis[3])

    cx = p1 + int((p3 - p1)/2)
    cy = p2 + int((p4 - p2)*1.5)
    w = 50
    h = 50
    x1 = cx - int(w/2)
    y1 = cy - int(h/2)
    x2 = cx + int(w/2)
    y2 = cy + int(h/2)
    crop_img = orin_img[y1:y2, x1:x2]
    return crop_img

def cri(v):
    m = np.zeros([66,66,3],np.uint8)
    m[2:64,2:64,0]=(v[0]*255)
    m[2:64,2:64,1]=(v[1]*255)
    m[2:64,2:64,2]=(v[2]*255)
    return m


if __name__ == "__main__":
    args = parse_arguments()
    path='/home/xanxus/Desktop/368_data/img_out/data/data_0'
    files = ['0_0_out_0','0_0_out_1','0_0_out_2','0_0_out_3','0_0_out_4','0_0_out_5','0_0_out_6','0_0_out_7','0_0_out_8','0_0_out_9']
    # files = ['0_0_out_0']
    # files = fo.get_file(os.path.join(path,'imgs'))
    # files.sort(reverse=False)
    # print(files)
    out_dict={}
    
    for file in range(len(files)):
        iname = os.path.join(path,'imgs','{}.jpg'.format(files[file]))
        lname = os.path.join(path,'labels','{}.xml'.format(files[file]))
        
        # read img
        orin_img = cv2.imread(iname)
        
        # get label
        labels,axises=xo.get_label(lname)
        # print(file)
        
        
        if file % 5 == 0:
            print('update temp')
            temp_pixel_color={}
            temp_img=[]
            temp ={}
            index = 0 
            for label,axis in zip(labels,axises):
                
                if label == 'head':
                    label_img = get_label_img(orin_img,axis)
                    temp_img.append(label_img)
                    crop_img = get_pixel_img(orin_img,axis)

                    crop_img = crop_img.reshape(crop_img.shape[0]*crop_img.shape[1],crop_img.shape[2])
                        # print(crop_img.shape)

                    centers,labels = kmeano.op_k_means(crop_img)
                    ch_centers=[]
                    for idx in centers:
                        for idy in idx:
                            ch_centers.append(idy)
                        # print('{}_{}'.format(file,index))
                        # print('\ncenters:{}\n'.format(centers))
                        # print('\nlabels:{}\n'.format(labels))
                    lx = ch_centers + labels
                    temp['label_{}'.format(index)]=lx
                    temp_pixel_color["label_{}".format(index)]=centers
                            
                    index  = index + 1
        # print(temp)
        else :
            index = 0
            for img in range(len(temp_img)):
                cv2.namedWindow('temp_{}'.format(img),cv2.WINDOW_NORMAL)
                cv2.resizeWindow('temp_{}'.format(img),200,200)
                cv2.imshow('temp_{}'.format(img),temp_img[img])

                for ix in range(len(temp_pixel_color['label_{}'.format(img)])):

                    pix = cri(temp_pixel_color['label_{}'.format(img)][ix])
                    cv2.imshow('temp_{}_pixel_{}'.format(img,ix),pix)

            for label,axis in zip(labels,axises):
                if label == 'head':
                    
                    label_img = get_label_img(orin_img,axis)
                    crop_img = get_pixel_img(orin_img,axis)

                    crop_img = crop_img.reshape(crop_img.shape[0]*crop_img.shape[1],crop_img.shape[2])
                        # print(crop_img.shape)

                    centers,labels = kmeano.op_k_means(crop_img)
                    ch_centers=[]
                    for idx in centers:
                        for idy in idx:
                            ch_centers.append(idy)
                    lx = ch_centers + labels
                    result_dist=[]
                    for key in temp.keys():
                        tem=temp[key]
                        dist = distance.euclidean(tuple(lx),tuple(tem))
                        result_dist.append(dist)
                    print(result_dist)
                    cv2.namedWindow('input_img',cv2.WINDOW_NORMAL)
                    cv2.resizeWindow('input_img',200,200)
                    cv2.imshow('input_img',label_img)
                    for center in range(len(centers)):
                        p = cri(centers[center])
                        cv2.imshow('picxel_{}'.format(center),p)


                
                    cv2.waitKey(0)
                    cv2.destroyWindow('input_img')
                    for center in range(len(centers)):
                        cv2.destroyWindow('picxel_{}'.format(center))
                
            cv2.destroyAllWindows           
