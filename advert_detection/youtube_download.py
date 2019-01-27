import argparse
import subprocess


def downloader(yt_url):

    try:
        video_id = yt_url.split("=")[-1].split("&")[0]
        video_id = yt_url.split("?")[-1].split("=")[1]
        print("Video ID: ", video_id)
    except:
        return False

    # View list of format options available for download.
    cmd = "youtube-dl -F %s" % str(yt_url)
    print(cmd)
    p = subprocess.Popen(cmd.split(" "), stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (output, stderr) = p.communicate()

    print(output)

    # Download the 'best' format for mp4 format.
    cmd = "youtube-dl -o %s.%s -f best %s" % (video_id, "mp4", str(yt_url))
    print(cmd)
    p = subprocess.Popen(cmd.split(" "),
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (output, stderr) = p.communicate()

    print(output)

    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL of YouTube video to Download.",
                        required=True)
    args = parser.parse_args()

    downloader(args.url)
