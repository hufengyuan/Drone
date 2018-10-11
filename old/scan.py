from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import re
 
def decode(im) : 
  decodedObjects = pyzbar.decode(im)
  
  for obj in decodedObjects:
    #解码
    var = str(obj.data)
    #print('Type : ', obj.type)
    #print('Data : ', var[11:14],'\n')
    r = int(var[12:14])
    #保存为文件
    file = open(r'C:\Users\apple\Desktop\test\original.txt','r')
    lines = []
    for i in file:
      lines.append(i)
    file.close()
    n=str(var[11:14] + ' y'+'\n')
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

  im = cv2.imread(r'C:\Users\apple\Desktop\test\test pics\20081001-005.jpg')
 
  decodedObjects = decode(im)
  #display(im, decodedObjects)
  
