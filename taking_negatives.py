# from ultralytics import YOLO
import os,cv2
from pathlib import Path

videos_path=list(Path('/mnt/data11/projects/Shelf_retail/DATASET/extra_videos').glob('*'))
# model=YOLO('runs/detect/train7/weights/best.pt')

output_path='/mnt/data11/projects/Shelf_retail/DATASET/data_3'
os.makedirs(output_path,exist_ok=True)
for video_path in videos_path:
    video_stem=Path(video_path).stem
    cap=cv2.VideoCapture(video_path)
    x=0
    while True:
        ret,frame=cap.read()

        if not ret:
            print("Video finished")
            break

    # results=model.predict(frame)

    # conf=results[0].boxes.conf.cpu().numpy()
    # s=0
    # for i in conf:
    #     if i>80:
    #         s+=1
    # if s<=1:
        if x%20==0:
            cv2.imwrite(f'{output_path}/{video_stem}_frame_{x}.jpg',frame)   
        x+=1

