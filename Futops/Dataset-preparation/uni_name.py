import os
import shutil
import uuid

target = '/home/rajput/Desktop/Dataset_Preparation/Images/no_mask/'
for i in os.listdir(target):
	i_id = i.split('.')[-1]
	src = target+i
	dst = target+str(uuid.uuid4())+'.'+i_id
	print(dst)
	shutil.move(src,dst)
