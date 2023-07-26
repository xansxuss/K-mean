import os,cv2,argparse
import xml.etree.cElementTree as ET


    
def get_label(path):
    label_list=[]
    axis=[]
    # xml_name = os.path.join(path,'{}.xml'.format(name))
    tree=ET.parse(path)
    root=tree.getroot()
    if root.findall('object') :
        for i in root.iter('object'):
            label = i[0].text
            label_list.append(label)
            xmin,ymin,xmax,ymax=(x.text for x in i.find('bndbox'))
            axis.append([xmin,ymin,xmax,ymax])
        return label_list,axis

        


def get_size(path,name): 
    size=[]
    xml_name = os.path.join(path,'{}.xml'.format(name))
    tree=ET.parse(xml_name)
    root=tree.getroot()
    if root.findall('size') :
        width,height,depth=(x.text for x in root.find('size'))
        size.append(width)
        size.append(height)
    # else:
        # print(name)
        # print("no find label")
    return size

