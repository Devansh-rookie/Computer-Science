import subprocess


def get_codecs():
    cmd = 'ffmpeg -codecs'
    x = subprocess.check_output(cmd, shell=True)
    x = x.split(b'/n')
    for y in x:
        print(y)


get_codecs()
