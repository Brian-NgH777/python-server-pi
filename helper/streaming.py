import sys
import os
import threading
import subprocess

cmdStart = "nohup ffmpeg -rtsp_transport tcp -i %s -framerate 20 -s 320x240 -vcodec libx264 -f flv -flvflags no_duration_filesize -an %s >/dev/null 2>&1 &"

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
        # subprocess.call(['sudo','./stop_stream.sh'])
        subprocess.Popen(['sudo', '/root/kill.sh'])
    except subprocess.CalledProcessError as e:
        print("cmdStop", e.output)