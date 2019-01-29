### advert_detection
Advert detection using audio and visual processing techniques.


### pip3 install required packages:

You may want to run everything in a virtualenv.  In the project root directory:

$ virtualenv -p python3 .

Then activate:

$ source bin/activate

And to install requires packages:

$ pip3 install -r requirements.txt


### Install 'ffmpeg':
This code requires the 'ffmpeg' command-line utility to be installed
in order to work.

On Linux:
$ apt update && apt install -y ffmpeg

On Mac OS with Homebrew:
$ brew install ffmpeg


### Run youtube_download:

$ python3 youtube_download.py --url https://www.youtube.com/watch?v=yoZPVMEsbeQ


### Run video2spectrogram:

$ python3 video2spectrogram.py --vid_name Ag60ZF-IdKk.mp4 --out_name dummy.wav --t_start 1 --cut_length 10


### Docker: Build image:

In the directory containing the Dockerfile, do:

$ docker build --tag advert_detection .

Run a container:

$ docker run -it advert_detection bash


### Run with docker-compose

Install docker and docker-compose following the official documentation:

1. Docker:
https://docs.docker.com/install/linux/docker-ce/ubuntu/
This installation process takes maybe 10 minutes, but you just copy/paste
the instructions on that page into terminal/terminator.

2. Docker Compose:
https://docs.docker.com/compose/install/#install-compose
Again, just follow the instructions.

To run docker without sudo, you need to create the docker group:

1. Create the docker group.
$ sudo groupadd docker

2. Add your user to the docker group.
$ sudo usermod -aG docker $USER

3. Log out and log back in so that your group membership is re-evaluated.

4. Verify that you can run docker commands without sudo.
$ docker run hello-world

Now you can do:

$ docker-compose up

If you have made edits to the Dockerfile, then you need to rebuild the image:

$ docker-compose up --build


### Manual testing of REST API

Try out the 'yt2melspec' route/endpoint:

$ curl localhost:6060/yt2melspec?url=https://www.youtube.com/watch?v=ilNEqmfUyzI

Try the 'testjson' route/endpoint:

$ curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"url":"https://www.youtube.com/watch?v=ilNEqmfUyzI"}' \
  localhost:6060/testjson
