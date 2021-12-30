import sys
import os
import threading
import subprocess

cmdStart = "nohup ffmpeg -fflags nobuffer -rtsp_transport tcp -i %s -framerate 20 -video_size 480x320 -vcodec libx264 -preset veryfast -maxrate 1984k -bufsize 3968k -vf \"format=yuv420p\" -g 60 -c:a aac -b:a 128k -ar 44100 -f flv %s &"

def thread_function(rtsp, rtmp):
    try:
        r = cmdStart%(rtsp, rtmp)
        subprocess.Popen(r, shell=True)
    except subprocess.CalledProcessError as e:
        print("cmdStop", e.output)
   
def start(rtsp, rtmp):
    x = threading.Thread(target=thread_function, args=(rtsp, rtmp))
    #  x.daemon = True
    x.start()

def stop():
    try:
        subprocess.Popen(['sudo','stop_stream.sh'])
    except subprocess.CalledProcessError as e:
        print("cmdStop", e.output)