### advert_detection
Advert detection using audio and visual processing techniques.

### pip3 install required packages:

You may want to run everything in a virtualenv.  In the project root directory:

$ virtualenv -p python3 .

Then activate:

$ source bin/activate

And to install requires packages:

$ pip3 install -r requirements.txt


### Install 'ffmpeg'
This code requires the 'ffmpeg' command-line utility to be installed
in order to work.

To install 'ffmpeg' on Mac OS with Homebrew:
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