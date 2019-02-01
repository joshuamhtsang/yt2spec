from flask_restful import Api
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS

from youtube_download import downloader
from audio_ninja import extract_wav, audio_cut
from video2spectrogram import audio2spectrogram

app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route("/echo_x")
def returnx():
    x = request.args.get("x", default=None, type=int)

    return jsonify({
        "x": x
    })


@app.route("/yt2melspec")
def yt2melspec():
    yt_url = request.args.get("url", default=None, type=str)

    video_filename = downloader(yt_url)
    print("Video %s has been downloaded!" % video_filename)

    response = {
        "spec_url": "http://joshuatsang.net/blah"
    }

    return jsonify(response)


@app.route("/testjson", methods=['POST'])
def testjson():
    req_data = request.get_json()

    yt_url = req_data["url"]

    video_filename = downloader(yt_url)
    print("Video %s has been downloaded!" % video_filename)

    audio_filename = extract_wav(video_filename, video_filename.split(".")[0] + '.wav')
    # Restrict to first 60 seconds for now.
    audio_cut_filename = audio_cut(audio_filename, 1, 61, audio_filename.split(".")[0])
    spec_filename = audio2spectrogram(audio_cut_filename)

    spec_url = 'placeholder'

    response = {
        "url": yt_url,
        "spec_url": spec_url
    }

    return jsonify(response)


@app.route("/returnimg", methods=['GET'])
def return_img():

    img_url = url_for('static', filename='curry.png')

    response ={
        "img_url": img_url
    }

    #return jsonify(response)
    return '<img src=' + img_url + '>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="6060")
