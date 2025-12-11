from pathlib import Path
import os,shutil

# negative_labels=list(Path('/mnt/data11/projects/Shelf_retail/DATASET/creating_dataset/EMPTY_with_images/labels/train').glob('*.txt'))
all_labels=list(Path('/mnt/data11/projects/Shelf_retail/DATASET/creating_dataset/Editted_shelfs/changed_labels').glob("*.txt"))
images_path=list(Path('3220_with_images/images/train').glob('*.jpg'))

output_images='/mnt/data11/projects/Shelf_retail/DATASET/creating_dataset/Editted_shelfs/images_1'
# new_labels='/mnt/data11/projects/Shelf_retail/DATASET/creating_dataset/new_segment/_labels_1'
# os.makedirs(new_labels,exist_ok=True)
os.makedirs(output_images,exist_ok=True)

neg_stem=[]
labels_stem=[]
images_stem=[]
# for label in negative_labels:
#     neg_stem.append(label.stem)
for label_path in all_labels:
    labels_stem.append(label_path.stem)
#     with open(label_path,'r') as file:
#         txt_file=file.readlines()
#     if len(txt_file)>=3:
#         labels_stem.append(label_path.stem)
#         shutil.copy(label_path,new_labels)
print(len(labels_stem))
for path in images_path:
#     images_stem.append(path.stem)
    # # images_stem.append(path.stem)
    if path.stem in labels_stem:
        shutil.copy(path,output_images)
    if path.stem in neg_stem:
        shutil.copy(path,output_images)

# for path in list(Path(output_labels).glob("*.jpg")):
#     images_stem.append(path.stem)

# for i in all_labels:
#     if i.stem in images_stem:
#         shutil.copy(i,new_labels)