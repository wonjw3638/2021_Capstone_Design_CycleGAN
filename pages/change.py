import os
import glob

def change():
    img_path = r'C:\Users\BTLsub\realsite\media\input'
    filenames = glob.glob(img_path + '/*.png')
    new_name = '\원본.jpg'
    
    if len(filenames)>0:
        os.rename(filenames[0],img_path+new_name)
    else :
        _filenames = glob.glob(img_path + '/*.jpg')
        os.rename(_filenames[0],img_path+new_name)

