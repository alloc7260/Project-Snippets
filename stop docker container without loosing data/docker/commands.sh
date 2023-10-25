docker build -t stream_infer .
docker run --gpus all -e VIDEO_PATH="/app/vol/car4.mp4" -v /home/ubuntu/vol:/app/vol -v /home/ubuntu/video:/app/video stream_infer