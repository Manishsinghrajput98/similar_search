import os
import glob
import cv2
import os
import shutil
import sys
from threading import Thread
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True)
ap.add_argument("-c", "--cat_name", required=True)
args = vars(ap.parse_args())

video_folder = args["input"]
move_folder_name = args["cat_name"]



def filter_image(v_url):
    video_path = v_url
    video_path.replace(" ","_")
    id_path = data_folder + v_url.split("/")[-1].split(".")[0] + "/"
    if os.path.exists(id_path):
        shutil.rmtree(id_path)
        os.mkdir(id_path)
    else:
        os.mkdir(id_path)

    image_folder = id_path +  "images/"
    if os.path.exists(image_folder):
        shutil.rmtree(image_folder)
        os.mkdir(image_folder)
    else:
        os.mkdir(image_folder)

    cmd = "ffmpeg -i {} -vf fps=1 {}{}_%d.jpg".format(video_path,image_folder,v_url.split("/")[-1].split(".")[0])
    os.system(cmd)

    path = sorted(glob.glob(image_folder + "*.*"), key=os.path.getmtime)
    sample = None


    def find_hist(image):
        image = cv2.imread(image)
        hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8],
                            [0, 256, 0, 256, 0, 256])
        hist = cv2.normalize(hist, hist).flatten()
        return hist


    def find_match(hist1, hist2):
        d = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
        return d

    sample_array = []
    different = []
    last_change_detect_at = None
    first_find = False
    last_image = None
    for j,i in enumerate(path):
        if j==0:
            sample = find_hist(i)
            first_find = True
            last_image = i
        elif first_find==True:
            sample = find_hist(last_image)
            first_find = False
            last_image = i
        elif first_find==False:
            sample = find_hist(last_image)
            last_image = i

        process_match = find_hist(i)
        match_result = find_match(sample, process_match)
        if (match_result*100)<=80:
            different.append(i)
    for i in different:
        shutil.move(i,move_folder_name)
    shutil.rmtree(image_folder)

if os.path.exists(move_folder_name):
    shutil.rmtree(move_folder_name)
    os.mkdir(move_folder_name)
else:
    os.mkdir(move_folder_name)

all_videos = glob.glob(video_folder+"/*.*")
data_folder = "data/"
if os.path.exists(data_folder):
    shutil.rmtree(data_folder)
    os.mkdir(data_folder)
else:
    os.mkdir(data_folder)
print(all_videos)

for i in all_videos:
    t = Thread(target=filter_image,args=[i])
    t.start()
