import cv2
import numpy as np
from ultralytics import YOLO

# ---------------------------------------------------------
# CONFIG
# ---------------------------------------------------------

shelf_model_path = "runs/detect/train13/weights/best.pt"        # YOLO OD model
part_model_path  = "runs/detect/train15/weights/best.pt"       # YOLO Seg model

input_video  = "/mnt/data11/projects/Shelf_retail/DATASET/testing_videos/WIN_20251128_14_01_07_Pro.mp4"
output_video = "output_checked_8.mp4"

valid_divider_counts = [3, 5, 9, 11, 15, 8]

# ---------------------------------------------------------
# LOAD MODELS
# ---------------------------------------------------------

shelf_model = YOLO(shelf_model_path)
part_model  = YOLO(part_model_path)

# ---------------------------------------------------------
# SIMPLE SHELF TRACKER (IOU-BASED)
# ---------------------------------------------------------

class ShelfTracker:
    def __init__(self, iou_thresh=0.5):
        self.iou_thresh = iou_thresh
        self.tracks = {}      # track_id : {"bbox":(x1,y1,x2,y2), "status":{}}
        self.next_id = 1

    def iou(self, boxA, boxB):
        xA = max(boxA[0], boxB[0])
        yA = max(boxA[1], boxB[1])
        xB = min(boxA[2], boxB[2])
        yB = min(boxA[3], boxB[3])

        inter = max(0, xB - xA) * max(0, yB - yA)
        areaA = (boxA[2]-boxA[0]) * (boxA[3]-boxA[1])
        areaB = (boxB[2]-boxB[0]) * (boxB[3]-boxB[1])

        return inter / (areaA + areaB - inter + 1e-6)

    def update(self, detected_boxes):
        new_tracks = {}

        for box in detected_boxes:
            matched_id = None
            for tid, data in self.tracks.items():
                if self.iou(box, data["bbox"]) > self.iou_thresh:
                    matched_id = tid
                    break

            if matched_id is not None:
                new_tracks[matched_id] = self.tracks[matched_id]
                new_tracks[matched_id]["bbox"] = box
            else:
                new_tracks[self.next_id] = {"bbox": box, "status": None}
                self.next_id += 1

        self.tracks = new_tracks
        return self.tracks


tracker = ShelfTracker()

# ---------------------------------------------------------
# VIDEO READER & WRITER
# ---------------------------------------------------------

cap = cv2.VideoCapture(input_video)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
writer = cv2.VideoWriter(output_video, fourcc, fps, (w, h))

# ---------------------------------------------------------
# PROCESS VIDEO
# ---------------------------------------------------------

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect shelves
    shelves = shelf_model(frame)[0].boxes
    detected_boxes = []

    for s in shelves:
        x1, y1, x2, y2 = map(int, s.xyxy[0])
        detected_boxes.append((x1, y1, x2, y2))

    # Update tracker
    tracks = tracker.update(detected_boxes)

    # Process each tracked shelf
    for tid, data in tracks.items():
        x1, y1, x2, y2 = data["bbox"]
        crop = frame[y1:y2, x1:x2]

        # Detect parts inside shelf crop
        part_out = part_model(crop)[0]

        counts = {"Antiplifir": 0, "Bullnose": 0, "Divider": 0}

        for p in part_out.boxes:
            cls_name = part_model.names[int(p.cls[0])]
            if cls_name in counts:
                counts[cls_name] += 1

        # Build display label
        A = counts["Antiplifir"]
        B = counts["Bullnose"]
        D = counts["Divider"]

        if D!=0:

            label = f"D:{D+1} F"
        else:
            label="Missing part: Divider"

        # Color: red if something is wrong
        color = (0, 255, 0)
        if A == 0 or B == 0 or D not in valid_divider_counts:
            color = (0, 0, 255)

        # Draw shelf bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 3)

        # Draw text label
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 4)

    writer.write(frame)

cap.release()
writer.release()
print("Processing completed! Saved to:", output_video)
