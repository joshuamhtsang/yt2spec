import subprocess


# Cut out a section of audio.
def audio_cut(filename, t_start, cut_length, outname):
    cmd = "ffmpeg -ss %s -t %s -i %s %s" % (
            t_start,
            cut_length,
            filename,
            outname)
    p = subprocess.Popen(cmd.split(" "),
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (output, stderr) = p.communicate()
    print(output, stderr)
