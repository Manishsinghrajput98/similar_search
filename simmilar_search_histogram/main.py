import os
import glob
import cv2
import sys
import argparse
import uuid

images = "Database/"

im = sorted(glob.glob(images + "*.*"), key=os.path.getmtime)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True)
args = vars(ap.parse_args())

input_image = args["input"]

def find_match(hist1, hist2):
  match = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
  return match

def find_hist(image):
  image = cv2.imread(image)
  hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8],[0, 256, 0, 256, 0, 256])
  hist = cv2.normalize(hist, hist).flatten()
  return hist

in_image  = cv2.imread(input_image)

input_image = find_hist(input_image)

for j,i in enumerate(im):
  sample = find_hist(i)
  match_result = find_match(sample, input_image)
  if (match_result*100)>=70:
    print("===========match===========",(match_result*100))
    image = cv2.imread(i)
    cv2.imwrite("output/Image number{}.jpg".format(j), image)
    cv2.imshow("Input image :- ",in_image)
    cv2.imshow("Image number {}".format(j), image)
    cv2.waitKey(1000)
  else:
  	print("-----no match-----",(match_result*100))