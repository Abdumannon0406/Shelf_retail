from ultralytics import YOLO
from pathlib import Path
import os,cv2
model=YOLO('runs/detect/train7/weights/best.pt')

image_path=('Pasted image.png')
# print(len(image_path))images/train
output_folder="/mnt/data11/projects/Shelf_retail/DATASET/Cropped_shelf_test"
os.makedirs(output_folder,exist_ok=True)

resutls=model.predict(image_path)

keypoints=resutls[0].boxes.xyxy.cpu().numpy().astype(int)
# points=bbox['xyxy']
# print(len(keypoints))
image_stem=Path(image_path).stem

image=cv2.imread(image_path,cv2.COLOR_BGR2RGB)

for j in range(len(keypoints)):
    cropped_image=image[keypoints[j][1]:keypoints[j][3],keypoints[j][0]:keypoints[j][2]]
    cv2.imwrite(f'{output_folder}/{image_stem}_{j}.jpg',cropped_image)
    

