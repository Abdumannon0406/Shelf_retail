from ultralytics import YOLO

model=YOLO("runs/segment/train10/weights/best.pt")

results=model.predict('/mnt/data11/projects/Shelf_retail/DATASET/Cropped_shelf/BOX2-10F-6F-10F-12F-16F-6F_frame_905_0.jpg',save=True)

conf=results[0].masks

print(conf[0])