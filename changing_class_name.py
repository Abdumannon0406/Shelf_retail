import os

label_dir = "/mnt/data11/projects/Shelf_retail/DATASET/Datasets/Shelf_detection_dataset/labels/val"   # replace with your labels folder

for filename in os.listdir(label_dir):
    if filename.endswith(".txt"):
        file_path = os.path.join(label_dir, filename)

        new_lines = []
        with open(file_path, "r") as f:
            for line in f.readlines():
                parts = line.strip().split()

                if len(parts) == 5:  # class + x + y + w + h
                    if parts[0] == "4":
                        parts[0] = "0"

                new_lines.append(" ".join(parts))

        # overwrite with updated labels
        with open(file_path, "w") as f:
            f.write("\n".join(new_lines))

print("All labels updated successfully.")
