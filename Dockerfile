FROM python:3.7-slim
RUN apt update && apt install -y \
    python3-dev \
    python3-pip
COPY ./requirements.txt /usr/local/src/advert_detection/
RUN pip3 install -r /usr/local/src/advert_detection/requirements.txt