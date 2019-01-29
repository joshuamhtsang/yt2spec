from flask_restful import Api
from flask import Flask, request, jsonify
from flask_cors import CORS

from youtube_download import downloader

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

    url = req_data["url"]

    response = {
        "url": url
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="6060")
