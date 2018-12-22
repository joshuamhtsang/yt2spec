import argparse
import subprocess

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL of yYouTube video to Download.",
                        required=True)
    args = parser.parse_args()
    print(args.url)

    video_id = args.url.split("=")[-1]
    print(video_id)

    cmd = "youtube-dl -F %s" % str(args.url)
    print(cmd)
    p = subprocess.Popen(cmd.split(" "), stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (output, stderr) = p.communicate()

    print(output)

    cmd = "youtube-dl -o %s.%s -f 17 %s" % (video_id, "mp4", str(args.url))
    print(cmd)
    p = subprocess.Popen(cmd.split(" "),
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (output, stderr) = p.communicate()

    print(output)
