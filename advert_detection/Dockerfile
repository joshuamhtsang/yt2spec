FROM python:3.7-slim
RUN apt update && apt install -y \
    python3-dev \
    python3-pip \
    ffmpeg \
    curl
COPY ./requirements.txt /usr/local/src/advert_detection/
RUN pip3 install -r /usr/local/src/advert_detection/requirements.txt
RUN curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
RUN chmod a+rx /usr/local/bin/youtube-dl
COPY . /usr/local/src/advert_detection/
WORKDIR /usr/local/src/advert_detection/
