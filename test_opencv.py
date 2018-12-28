import ffmpeg
import cv2
import subprocess
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--vid_name", help="blah.",
                        required=True)
    args = parser.parse_args()
    
    print(args.vid_name)
    
    cmd = "ffmpeg -y -i %s -vn output.wav" % (args.vid_name)
    p = subprocess.Popen(cmd.split(" "),
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (output, stderr) = p.communicate()
    print(output, stderr)
    
    