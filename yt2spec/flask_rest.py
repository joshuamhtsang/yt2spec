from flask_restful import Api
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS

from youtube_download import downloader
from audio_ninja import extract_wav, audio_cut
from video2spectrogram import audio2spectrogram

import uuid
import os
import subprocess

app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route("/echo_x")
def returnx():
    x = request.args.get("x", default=None, type=int)

    return jsonify({
        "x": x
    })


@app.route("/yt2melspec", methods=['POST'])
def yt2melspec():
    req_data = request.get_json()
    yt_url = req_data["url"]

    # Download *.mp4 video file.
    video_filename = downloader(yt_url)
    print("Video %s has been downloaded!" % video_filename)

    # Extract *.wav from the *.mp4 file.
    audio_filename = extract_wav(video_filename, video_filename.split(".")[0] + '.wav')
    # Restrict to first 60 seconds for now.
    audio_cut_filename = audio_cut(audio_filename, 1, 61, audio_filename.split(".")[0])
    # Delete redundant *.mp4 and uncut *.mp4.
    cmd = "rm %s %s" % (str(video_filename), str(audio_filename))
    p = subprocess.Popen(cmd.split(" "), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (output, stderr) = p.communicate()
    print(output)

    # Compute Mel-spectrogram.
    spec_filename = audio2spectrogram(audio_cut_filename)

    # Rename the spectrogram to have UUID as name.
    print("spec_filename = ", spec_filename)
    uid = uuid.uuid4()
    uid_filename = str(uid) + '.' + spec_filename.split(".")[-1]
    os.rename('./' + spec_filename, './static/' + uid_filename)

    spec_url = url_for('static', filename=uid_filename)

    response = {
        "url": yt_url,
        "spec_url": spec_url
    }

    return jsonify(response)


@app.route("/returnimg", methods=['GET'])
def return_img():
    img_url = url_for('static', filename='curry.png')

    return '<img src=' + img_url + '>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="6060")
