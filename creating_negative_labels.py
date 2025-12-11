import os,shutil,cv2
from pathlib import Path

images_path=list(Path("/mnt/data11/projects/Shelf_retail/DATASET/creating_dataset/new_shelf_detection/images").glob("*"))
labels_path=list(Path('/mnt/data11/projects/Shelf_retail/DATASET/creating_dataset/new_shelf_detection/labels').glob('*'))
output_labels='/mnt/data11/projects/Shelf_retail/DATASET/creating_dataset/new_shelf_detection/negative_labels'
os.makedirs(output_labels,exist_ok=True)

# images_stem=[]
labels_stem=[]
for path in labels_path:
    labels_stem.append(path.stem)

for i in range(len(images_path)):

    image_stem=images_path[i].stem
    if image_stem not in labels_stem:
        open(f"{output_labels}/{image_stem}.txt",'w').close()