FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get -y install python3.9
RUN apt-get -y install python3-pip
RUN apt-get update && apt-get install libgl1 libgl1-mesa-glx  libglib2.0-0 -y

RUN pip3 install opencv-python-headless ultralytics

WORKDIR /app

COPY . .

CMD ["python3", "infer.py"]