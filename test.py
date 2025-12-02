from ultralytics import YOLO

model=YOLO('runs/detect/train11/weights/best.pt')

results=model.track('/mnt/data11/projects/Shelf_retail/DATASET/testing_videos/WIN_20251128_14_01_07_Pro.mp4',tracker='bytetrack.yaml',save=True,show=True)

# conf=results[0].boxes.conf.cpu().numpy()

# print(conf)