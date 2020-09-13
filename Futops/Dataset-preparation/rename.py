import os 
def main(): 
  
    for count, filename in enumerate(os.listdir("/home/rajput/Desktop/Dataset_Preparation/xmls")): 
        dst ="new" + str(count) + ".xml"
        src ='/home/rajput/Desktop/Dataset_Preparation/xmls/'+ filename 
        dst ='/home/rajput/Desktop/Dataset_Preparation/xmls/'+ dst 
        os.rename(src, dst) 

if __name__ == '__main__': 
    main() 