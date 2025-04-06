import cv2

def extract_info_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    info_list = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Example: process every 30th frame
        frame_count += 1
        if frame_count % 30 == 0:
            info_list.append(f"Processed frame {frame_count}")

    cap.release()
    return info_list
