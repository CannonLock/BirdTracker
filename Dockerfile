FROM python:3.9.8

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY . /app
WORKDIR /app

CMD python3 bird_parser/bird_tracker/processing.py

