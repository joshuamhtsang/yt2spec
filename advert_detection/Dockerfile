FROM python:3.7-slim
RUN apt update && apt install -y \
    python3-dev \
    python3-pip \
    ffmpeg \
    curl
COPY ./requirements.txt /usr/local/src/advert_detection/
RUN pip3 install -r /usr/local/src/advert_detection/requirements.txt
RUN pip3 install --upgrade youtube-dl
COPY . /usr/local/src/advert_detection/
WORKDIR /usr/local/src/advert_detection/
ENV PYTHONPATH="${PYTHONPATH}:/usr/local/src/advert_detection/advert_detection"