import cv2
import os
import signal
import sys
from ultralytics import YOLO


video_path = os.environ.get("VIDEO_PATH")
# video_path = "../vol/car4.mp4"

video_out = "/app/video/outvideo.mp4"
# video_out = "../video/outvideo.mp4"

model = YOLO('/app/vol/yolov8n.pt')
# model = YOLO(../vol/yolov8n.pt')


def release_resources(signal, frame):
    print("Received termination signal.")
    out.release()
    cap.release()
    sys.exit(0)

def get_video_info(filename):
    f = cv2.VideoCapture(filename)
    video_width = int(f.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_height = int(f.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(f.get(cv2.CAP_PROP_FPS))
    TNF = int(f.get(cv2.CAP_PROP_FRAME_COUNT))  # total number of frames
    rval, frame = f.read()
    image = frame
    f.release()
    return image, int(fps), video_width, video_height, TNF


image, fps, video_width, video_height, tnf = get_video_info(video_path)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(video_out, fourcc, fps, (video_width, video_height))

cap = cv2.VideoCapture(video_path)
frame_count = 0

signal.signal(signal.SIGTERM, release_resources)

while True:
    ret, frame = cap.read()
    if not ret: break
    frame_count += 1

    result = model(frame)[0]

    out.write(result.plot())
    print(frame_count)


# Release the video file
out.release()
cap.release()

print("Completed without termination signal.")