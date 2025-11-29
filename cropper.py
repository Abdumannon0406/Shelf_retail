from ultralytics import YOLO
from pathlib import Path
import os,cv2
model=YOLO('runs/detect/train7/weights/best.pt')

image_path=list(Path('/mnt/data11/projects/Shelf_retail/DATASET/Shelf_detection_dataset/images/train').glob('*.jpg'))
# print(len(image_path))
output_folder="/mnt/data11/projects/Shelf_retail/DATASET/Cropped_shelf"
os.makedirs(output_folder,exist_ok=True)

for i in range(len(image_path)):

    resutls=model.predict(image_path[i])

    keypoints=resutls[0].boxes.xyxy.cpu().numpy().astype(int)
    # points=bbox['xyxy']
    # print(len(keypoints))
    image_stem=image_path[i].stem

    image=cv2.imread(image_path[i],cv2.COLOR_BGR2RGB)

    for j in range(len(keypoints)):
        cropped_image=image[keypoints[j][1]:keypoints[j][3],keypoints[j][0]:keypoints[j][2]]
        cv2.imwrite(f'{output_folder}/{image_stem}_{j}.jpg',cropped_image)
    

