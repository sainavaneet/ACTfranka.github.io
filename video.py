import cv2
import os

def extract_frames(video_path, output_folder):
    # Make sure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load the video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    fps = int(cap.get(cv2.CAP_PROP_FPS))  # Frames per second
    if fps == 0:
        print("Error: FPS is zero, which suggests a problem with video loading.")
        return

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # Total frames
    duration = frame_count / fps  # Duration of video in seconds

    print(f"FPS: {fps}")
    print(f"Total frames: {frame_count}")
    print(f"Duration: {duration} seconds")

    success, frame = cap.read()
    count = 0
    frame_id = 0

    while success:
        # Capture frames every 0.2 second to make 5 images per second
        if count % (fps // 5) == 0:
            resized_frame = cv2.resize(frame, (536, 865))
            # Save frame as JPEG file
            filename = f"{output_folder}/{frame_id:06}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Saved: {filename}")
            frame_id += 1

        success, frame = cap.read()
        count += 1

    cap.release()
    print("Done extracting frames.")

# Usage
video_path = r'C:\Users\saina\OneDrive\Desktop\xampp\htdocs\assets\task.mp4'

output_folder = 'static\interpolation\stacked'  # Folder to save frames
extract_frames(video_path, output_folder)
