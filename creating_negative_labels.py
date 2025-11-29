import os,shutil,cv2
from pathlib import Path

images_path=list(Path("/mnt/data11/projects/Shelf_retail/DATASET/Negatives/images").glob("*"))
output_labels='/mnt/data11/projects/Shelf_retail/DATASET/Negatives/labels'
images_stem=[]

for i in range(len(images_path)):
    image_stem=images_path[i].stem
    open(f"{output_labels}/{image_stem}.txt",'w').close()