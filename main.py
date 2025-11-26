from pathlib import Path
import os,cv2

videos_folder=list(Path('/mnt/data11/projects/Shelf_retail/DATASET/videos').glob('*.mp4'))
# print(len(videos_folder))
output_path='/mnt/data11/projects/Shelf_retail/DATASET/Dataset'
os.makedirs(output_path,exist_ok=True)

for video_path in videos_folder:

    # Extract only the filename without extension
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    # Create folder for each video
    save_dir = f"{output_path}/{video_name}"
    os.makedirs(save_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Cannot open {video_path}")
        continue

    frame_index = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            print(f"Finished video: {video_path}")
            break
        if frame_index%5==0:
            save_path = f"{save_dir}/{video_name}_frame_{frame_index}.jpg"
            cv2.imwrite(save_path, frame)
        frame_index += 1

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()

cv2.destroyAllWindows()