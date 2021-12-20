import subprocess

cmd = "ffmpeg -i %s -vframes 1 %s"

def snapshot(rtsp, path):
    try:
        r = cmd%(rtsp, path)
        subprocess.check_output(r, shell=True).decode("utf-8")
        return True
    except subprocess.CalledProcessError as e:
        print(e.output)
        return False

def new(rtsp, path):
    return snapshot(rtsp, path)
