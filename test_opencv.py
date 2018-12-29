import ffmpeg
import cv2
import subprocess
import argparse
import librosa
import librosa.display
import matplotlib
import matplotlib.pyplot as plt

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--vid_name", help="blah.",
                        required=True)
    parser.add_argument("--out_name", help="blah.",
                        required=True)
    args = parser.parse_args()
    
    print(args.vid_name)
    
    cmd = "ffmpeg -i %s -vn %s" % (args.vid_name, args.out_name)
    p = subprocess.Popen(cmd.split(" "),
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (output, stderr) = p.communicate()
    print(output, stderr)
    
    cmd = "ffmpeg -ss 0 -t 100 -i %s %s" % (
            args.out_name, 
            args.out_name.split(".")[0] + "_100.wav")
    p = subprocess.Popen(cmd.split(" "),
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (output, stderr) = p.communicate()
    print(output, stderr)
    
    y, sr = librosa.load(args.out_name.split(".")[0] + "_100.wav")
    S = librosa.feature.melspectrogram(y=y, sr=sr, fmax=1000)
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(librosa.power_to_db(S), y_axis='mel', x_axis='time')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel spectrogram')
    plt.tight_layout()
    #plt.show()
    plt.savefig('./spec.png')
    plt.close()
    
    yft = librosa.core.stft(y)
    print(yft)
    print(yft.shape)
    
    