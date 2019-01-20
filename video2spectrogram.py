import subprocess
import argparse
import librosa
import librosa.display
import matplotlib
import matplotlib.pyplot as plt
import audio_ninja
import os


def audio2spectrogram(audio_filename):
    spec_filename = "spec_" + audio_filename.split(".")[0]

    y, sr = librosa.load(audio_filename)
    S = librosa.feature.melspectrogram(y=y, sr=sr, fmax=1000)
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(librosa.power_to_db(S), y_axis='mel', x_axis='time')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel spectrogram')
    plt.tight_layout()
    # plt.show()
    plt.savefig(spec_filename.split(".")[0] + '.png')
    plt.close()

    yft = librosa.core.stft(y)
    print(yft)
    print(yft.shape)

    return spec_filename


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--vid_name", help="Video file to process.",
                        required=True)
    parser.add_argument("--out_name", help="Name of extracted audio file (something.wav).",
                        required=True)
    parser.add_argument("--t_start", help="Start time of audio cut-out.")
    parser.add_argument("--cut_length", help="Length, in seconds, of audio to cut out.")
    args = parser.parse_args()
    
    print("Input video name: " + args.vid_name)

    # Extract audio *.wav from the video file.
    audio_ninja.extract_wav(
        args.vid_name,
        args.out_name
    )

    # Cut out a section of audio.
    outname_final = audio_ninja.audio_cut(
        args.out_name,
        args.t_start,
        args.cut_length,
        args.out_name
    )

    audio2spectrogram(outname_final)

    # Clean up.
    os.remove(outname_final)
