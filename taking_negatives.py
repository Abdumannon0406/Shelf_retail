from ultralytics import YOLO
import os,cv2
from pathlib import Path


model=YOLO('runs/detect/train7/weights/best.pt')

output_path='/mnt/data11/projects/Shelf_retail/DATASET/positive_data_3'
os.makedirs(output_path,exist_ok=True)
video_stem=Path("/mnt/data11/projects/Shelf_retail/DATASET/extra_videos/WIN_20251128_14_44_27_Pro.mp4").stem
cap=cv2.VideoCapture("/mnt/data11/projects/Shelf_retail/DATASET/extra_videos/WIN_20251128_14_44_27_Pro.mp4")
x=0
while True:
    ret,frame=cap.read()

    if not ret:
        print("Video finished")
        break

    results=model.predict(frame)

    conf=results[0].boxes.conf.cpu().numpy()
    # s=0
    # for i in conf:
    #     if i>80:
    #         s+=1
    # if s<=1:
    if x%10==0:
        cv2.imwrite(f'{output_path}/{video_stem}_frame_{x}.jpg',frame)   
    x+=1

