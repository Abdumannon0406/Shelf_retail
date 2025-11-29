import shutil,os
from pathlib import Path

labels=list(Path('/mnt/data11/projects/Shelf_retail/DATASET/Shelf_detection_dataset/labels/train').glob("*.txt"))
images=list(Path('/mnt/data11/projects/Shelf_retail/DATASET/Shelf_detection_dataset/images').glob("*jpg"))

val_labels='/mnt/data11/projects/Shelf_retail/DATASET/Shelf_detection_dataset/labels/val'
val_images='/mnt/data11/projects/Shelf_retail/DATASET/Shelf_detection_dataset/images/val'
train_iamges='/mnt/data11/projects/Shelf_retail/DATASET/Shelf_detection_dataset/images/train'

os.makedirs(val_labels,exist_ok=True)
os.makedirs(val_images,exist_ok=True)
os.makedirs(train_iamges,exist_ok=True)

s=0
val_stem=[]
train_stem=[]
for label in labels:
    if s%13==0:
        shutil.move(label,val_labels)
        val_stem.append(label.stem)
    else:
        train_stem.append(label.stem)
    s+=1


for image_path in images:
    if image_path.stem in val_stem:
        shutil.move(image_path,val_images)
    elif image_path.stem in train_stem:
        shutil.move(image_path,train_iamges)
    
