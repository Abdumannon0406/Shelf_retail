import os
import shutil
from pathlib import Path

# v1_dir = list(Path("/home/codeschool/Abdumannon/Shelf_retail/3220_with_images/labels/train").glob('*'))
v2_dir = list(Path("/mnt/data11/projects/Shelf_retail/DATASET/creating_dataset/Editted_shelfs/Komil_editted/labels/train").glob("*"))
# v2_folder=list(Path('testing_txt').glob("*.txt"))
# v1_folder = "/home/codeschool/Abdumannon/Shelf_retail/3220_with_images/labels/train"
# v2_folder = "/mnt/data11/projects/Shelf_retail/DATASET/creating_dataset/Editted_shelfs/Asadbek_edited/labels/train"
output_folder = "/mnt/data11/projects/Shelf_retail/DATASET/creating_dataset/Editted_shelfs/changed_labels_2"


os.makedirs(output_folder, exist_ok=True)

v1_stems=[]
v2_stems=[]
# for path in v1_folder:
#     v1_stems.append(path.stem)

for path in v2_dir:
    # v2_stems.append(path.stem)

    with open(path,'r') as file:
        data=file.readlines()

        for line in data:
            splitted_line=line.split()
            if (splitted_line[0]=='4' or '0') and len(splitted_line)<15:

                shutil.copy(path,output_folder)


