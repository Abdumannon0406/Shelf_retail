from ultralytics import YOLO
import os
import numpy as np

model=YOLO("runs/segment/train10/weights/best.pt")

image_folder = "3680_with images/images/train/"
results = model(image_folder, stream=True)

os.makedirs("3680_with images/labels/train", exist_ok=True)

for r in results:
    img_name = os.path.basename(r.path).split('.')[0]
    txt_path = f"3680_with images/labels/train/{img_name}.txt"

    h, w = r.orig_shape

    with open(txt_path, "w") as f:
        for box, mask in zip(r.boxes, r.masks.xyn):
            cls = int(box.cls)

            # mask contains polygon points in absolute pixel coords (Nx2)
            polygon = mask.reshape(-1, 2)

            # flatten Nx2 → x1 y1 x2 y2 ... xn yn
            flat = polygon.flatten()

            # convert to string
            poly_str = " ".join(f"{v:.6f}" for v in flat)

            # write YOLO segmentation line
            f.write(f"{cls} {poly_str}\n")

    print(f"Saved: {txt_path}")
