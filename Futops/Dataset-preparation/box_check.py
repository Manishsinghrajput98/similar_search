import glob
import cv2
import os

classes=["mask","no"]

txt_path = "Final_Dataset_yolov3/"
image_path_dir = "Final_Dataset_yolov3/"


for i in glob.glob(txt_path+"/*.txt"):
    f = open(i)
    lines = f.readlines()
    
    image_path = image_path_dir +i.split("/")[-1].split(".")[0]+".jpg"
    print(image_path)
    if not os.path.exists(image_path):
       image_path = image_path_dir +i.split("/")[-1].split(".")[0]+".png"
       if not os.path.exists(image_path):
           continue
    im = cv2.imread(image_path)
    h,w,c = im.shape
    for line in lines:
        line = line[0:-1]
        data = line.split(" ")
        
        class_index = int(data[0])
        bbox = [float(k) for k in data[1:]]
        
        _w = int(bbox[2]*w)
        _h = int(bbox[3]*h)
        _x = int(bbox[0]*w - _w/2)
        _y = int(bbox[1]*h - _h/2)  
        cv2.rectangle(im,(_x,_y),(_x+_w,_y+_h),(0,0,255),2)
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        cv2.putText(im,classes[class_index],(_x,_y),font,1,(0,255,255),1)
        print(bbox)
    cv2.imshow("img",im)
    cv2.waitKey(0)
