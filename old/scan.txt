from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import time
import shutil
import os

def listdir(path, list_name): 
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        else:
             list_name.append((file_path,os.path.getctime(file_path)))

def newestfile(target_list):
    newest_file = target_list[0]
    for i in range(len(target_list)):
        if i < (len(target_list)-1) and newest_file[1] < target_list[i+1][1]:
            newest_file = target_list[i+1]
        else:
            continue
    #print('newest file is',newest_file)
    return newest_file
p = r'C:\Users\apple\Desktop\test\test pics'
list = []
listdir(p, list)
new_file = newestfile(list)
#print('from:',new_file[0])

def decode(im) : 
  decodedObjects = pyzbar.decode(im)
  
  for obj in decodedObjects:
    #解码
    var = str(obj.data)
    #print('Type : ', obj.type)
    #print('Data : ', var[11:14],'\n')
    r = int(var[12:14])
    #保存为文件
    file = open(r'C:\Users\apple\Desktop\test\result.txt','r')
    lines = []
    for i in file:
      lines.append(i)
    file.close()
    n=str(var[11:14] + ' y ' + str(time.strftime('%Y:%m:%d:%H:%M:%S',time.localtime(time.time()))) +'\n')
    lines.pop(r-1)
    lines.insert(r-1,n)
    file_write_obj = open(r'C:\Users\apple\Desktop\test\result.txt', 'w')
    for var in lines:
      file_write_obj.writelines(var)
    file_write_obj.close()
  return decodedObjects
 
 
def display(im, decodedObjects):
  #显示图片
  for decodedObject in decodedObjects: 
    points = decodedObject.polygon
    if len(points) > 4 : 
      hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
      hull = list(map(tuple, np.squeeze(hull)))
    else : 
      hull = points;  
    n = len(hull)
    for j in range(0,n):
      cv2.line(im, hull[j], hull[ (j+1) % n], (255,0,0), 3)
  cv2.namedWindow("Results",0);
  cv2.resizeWindow("Results", 1280, 960);
  cv2.imshow("Results", im);
  cv2.waitKey(0);
 

#主程序
if __name__ == '__main__':
  pic = new_file[0]
  im = cv2.imread(str(pic))
  decodedObjects = decode(im)
  display(im, decodedObjects)
  
