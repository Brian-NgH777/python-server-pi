import subprocess

cmd = "ffmpeg -i %s -vframes 1 %s" # ffmpeg -i rtsp://admin:Viact123@192.168.92.110:554/live -vframes 1 image.jpg

def snapshot(rtsp, pathFile):
    try:
        r = cmd%(rtsp, pathFile)
        subprocess.check_output(r, shell=True)
    except subprocess.CalledProcessError as e:
        return e.output

def new(rtsp, pathFile):
    return snapshot(rtsp, pathFile)
