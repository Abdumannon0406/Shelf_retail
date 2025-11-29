from ultralytics import YOLO

model=YOLO("yolo11n.pt")

results=model.train(data='/mnt/data11/projects/Shelf_retail/DATASET/Shelf_detection_dataset/data.yaml',epochs=200)