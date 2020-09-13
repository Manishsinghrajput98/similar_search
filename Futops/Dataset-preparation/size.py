import os
import cv2
dir_path="/home/rajput/Desktop/Dataset_Preparation/Images/no_mask/"
for img_path in os.listdir(dir_path):
   complete_path=os.path.join(dir_path,img_path)
   print(complete_path)
   img=cv2.imread(complete_path)
   h,w,c=img.shape
   #scale=1058./w
   scale=640./h
   if scale<1:
       img = cv2.resize(img,None,fx=scale,fy=scale,interpolation = cv2.INTER_CUBIC)
       cv2.imwrite(complete_path,img)
