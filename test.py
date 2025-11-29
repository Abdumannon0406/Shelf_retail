from ultralytics import YOLO

model=YOLO('runs/detect/train11/weights/best.pt')

results=model.track('/mnt/data11/projects/Shelf_retail/DATASET/testing_videos',tracker='bytetrack.yaml',save=True,show=True,conf=0.7)

# conf=results[0].boxes.conf.cpu().numpy()

# print(conf)