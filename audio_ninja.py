import subprocess


def extract_wav(filename, outname):
    cmd = "ffmpeg -i %s -vn %s" % (filename, outname)
    p = subprocess.Popen(cmd.split(" "),
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (output, stderr) = p.communicate()
    print(output, stderr)


# Cut out a section of audio.
def audio_cut(filename, t_start, cut_length, outname):
    outname_final = '%s_%s_%s.wav' % (outname.split(".")[0], str(t_start), str(cut_length))

    cmd = "ffmpeg -ss %s -t %s -i %s %s" % (
            t_start,
            cut_length,
            filename,
            outname_final)
    p = subprocess.Popen(cmd.split(" "),
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (output, stderr) = p.communicate()
    print(output, stderr)

    return outname_final
