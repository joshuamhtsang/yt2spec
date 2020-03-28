import argparse
import subprocess


def downloader(yt_url):
    # Remove extraneous parameters in YouTube URL.
    yt_url = yt_url.split("&")[0]

    try:
        video_id = yt_url.split("?")[-1].split("=")[1]
        print("Video ID: ", video_id)
    except Exception as e:
        " !!!ERROR!!! Error when parsing the YouTube URL to extract the video id."
        raise e

    # View list of format options available for download.
    cmd = "youtube-dl -F %s" % str(yt_url)
    print(cmd)
    try:
        p = subprocess.Popen(
            cmd.split(" "),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        (output, stderr) = p.communicate()
        print(output)
        if p.returncode != 0:
            raise RuntimeError(stderr)
    except Exception as e:
        " !!!ERROR!!! Error when retrieving format options for a video on YouTube."
        print(e)
        raise e

    # Download the 'best' format for mp4 format.
    filename = "%s.%s" % (video_id, "mp4")

    cmd = "youtube-dl -o %s -f best %s" % (filename, str(yt_url))
    print(cmd)
    try:
        p = subprocess.Popen(
            cmd.split(" "),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        (output, stderr) = p.communicate()
        print(output)
        if p.returncode != 0:
            raise RuntimeError(stderr)
    except Exception as e:
        " !!!ERROR!!! Error when downloading video from YouTube using youtube-dl."
        print(e)
        raise e

    return filename


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL of YouTube video to Download.",
                        required=True)
    args = parser.parse_args()

    downloader(args.url)
