import os,json,cv2
import numpy as np
from scipy.spatial import distance
def show_img(name,img):
    cv2.namedWindow(name,cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name,200,200)
    cv2.imshow(name,img)
   

def cri(n,v):
    m = np.zeros([66,66,3],np.uint8)
    m[2:64,2:64,0]=(v[0]*255)
    m[2:64,2:64,1]=(v[1]*255)
    m[2:64,2:64,2]=(v[2]*255)
    show_img('{}'.format(n),m)

def draw(n,l):

    for v in l:
        cri('{}'.format(n),v)
            

cv2.waitKey(0)
cv2.destroyAllWindows()
c = 0.05
with open('./out_result_1.json','r') as f:
    data = json.load(f)
f.close
v={}
keys = data.keys()
l=[]
for key in keys:
    for label in data["{}".format(key)]:
        listss = []
        for value in data["{}".format(key)].get(label):
            
            # print(type(value))
            if isinstance(value,list):
                for i in value:
                    listss.append(i)
            else:
                listss.append(value)
    
        v['{}_{}'.format(key,label)]=listss
# print(v.keys())
    

# v00 = [data['0_0_out_0'].get('label_0')[3],data['0_0_out_0'].get('label_0')[4],data['0_0_out_0'].get('label_0')[5]]
v00 = [data['0_0_out_0'].get('label_0')[0][0],data['0_0_out_0'].get('label_0')[0][1],data['0_0_out_0'].get('label_0')[0][2],data['0_0_out_0'].get('label_0')[1][0],data['0_0_out_0'].get('label_0')[1][1],data['0_0_out_0'].get('label_0')[1][2],data['0_0_out_0'].get('label_0')[2][0],data['0_0_out_0'].get('label_0')[2][1],data['0_0_out_0'].get('label_0')[2][2],data['0_0_out_0'].get('label_0')[3],data['0_0_out_0'].get('label_0')[4],data['0_0_out_0'].get('label_0')[5]]
v01 = [data['0_0_out_0'].get('label_1')[0][0],data['0_0_out_0'].get('label_1')[0][1],data['0_0_out_0'].get('label_1')[0][2],data['0_0_out_0'].get('label_1')[1][0],data['0_0_out_0'].get('label_1')[1][1],data['0_0_out_0'].get('label_1')[1][2],data['0_0_out_0'].get('label_1')[2][0],data['0_0_out_0'].get('label_1')[2][1],data['0_0_out_0'].get('label_1')[2][2],data['0_0_out_0'].get('label_1')[3],data['0_0_out_0'].get('label_1')[4],data['0_0_out_0'].get('label_1')[5]]
v02 = [data['0_0_out_0'].get('label_2')[0][0],data['0_0_out_0'].get('label_2')[0][1],data['0_0_out_0'].get('label_2')[0][2],data['0_0_out_0'].get('label_2')[1][0],data['0_0_out_0'].get('label_2')[1][1],data['0_0_out_0'].get('label_2')[1][2],data['0_0_out_0'].get('label_2')[2][0],data['0_0_out_0'].get('label_2')[2][1],data['0_0_out_0'].get('label_2')[2][2],data['0_0_out_0'].get('label_2')[3],data['0_0_out_0'].get('label_2')[4],data['0_0_out_0'].get('label_2')[5]]
    
# v90 = [data['0_0_out_9'].get('label_0')[3],data['0_0_out_9'].get('label_1')[4],data['0_0_out_9'].get('label_2')[5]]
v90 = [data['0_0_out_9'].get('label_0')[0][0],data['0_0_out_9'].get('label_0')[0][1],data['0_0_out_9'].get('label_0')[0][2],data['0_0_out_9'].get('label_0')[1][0],data['0_0_out_9'].get('label_0')[1][1],data['0_0_out_9'].get('label_0')[1][2],data['0_0_out_9'].get('label_0')[2][0],data['0_0_out_9'].get('label_0')[2][1],data['0_0_out_9'].get('label_0')[2][2],data['0_0_out_9'].get('label_0')[3],data['0_0_out_9'].get('label_0')[4],data['0_0_out_9'].get('label_0')[5]]
v91 = [data['0_0_out_9'].get('label_1')[0][0],data['0_0_out_9'].get('label_1')[0][1],data['0_0_out_9'].get('label_1')[0][2],data['0_0_out_9'].get('label_1')[1][0],data['0_0_out_9'].get('label_1')[1][1],data['0_0_out_9'].get('label_1')[1][2],data['0_0_out_9'].get('label_1')[2][0],data['0_0_out_9'].get('label_1')[2][1],data['0_0_out_9'].get('label_1')[2][2],data['0_0_out_9'].get('label_1')[3],data['0_0_out_9'].get('label_1')[4],data['0_0_out_9'].get('label_1')[5]]
v92 = [data['0_0_out_9'].get('label_2')[0][0],data['0_0_out_9'].get('label_2')[0][1],data['0_0_out_9'].get('label_2')[0][2],data['0_0_out_9'].get('label_2')[1][0],data['0_0_out_9'].get('label_2')[1][1],data['0_0_out_9'].get('label_2')[1][2],data['0_0_out_9'].get('label_2')[2][0],data['0_0_out_9'].get('label_2')[2][1],data['0_0_out_9'].get('label_2')[2][2],data['0_0_out_9'].get('label_2')[3],data['0_0_out_9'].get('label_2')[4],data['0_0_out_9'].get('label_2')[5]]



dist1 = distance.euclidean(tuple(v00),tuple(v90))
print(dist1)

dist2 = distance.euclidean(tuple(v00),tuple(v91))
print(dist2)

dist3 = distance.euclidean(tuple(v00),tuple(v92))
print(dist3)

# l1 = [[0.3418275122549019,0.314319087009804,0.22366727941176476],
#                [
#                     0.32677934410903636,
#                     0.29812778310822446,
#                     0.20592417644598615
#                ],
#                [
#                     0.31511738716105,
#                     0.285483265471137,
#                     0.1892922117300529
#                ]]
# for i in range(len(l1)):
#     cri('l1_label_{}'.format(i),l1[i])
# l2 = [[
#                     0.3134257638982368,
#                     0.2740467537129268,
#                     0.2257441557858841
#                ],
#                [
#                     0.578143550998381,
#                     0.6304191401331173,
#                     0.622719913653535
#                ],
#                [
#                     0.46642409541136043,
#                     0.45195067717808773,
#                     0.42397412573276727
#                ]]

# for i in range(len(l2)):
#     cri('l2_label_{}'.format(i),l2[i])

# l3 = [[
#                     0.4137254901960783,
#                     0.3934862080425389,
#                     0.36115653040877416
#                ],
#                [
#                     0.3201146928490744,
#                     0.3993280620963303,
#                     0.5227676890549426
#                ],
#                [
#                     0.49509956393132676,
#                     0.5474522001646691,
#                     0.5896929222699967
#                ]]
# for i in range(len(l3)):
#     cri('l3_label_{}'.format(i),l3[i])
# cv2.waitKey(0)
# cv2.destroyAllWindows()