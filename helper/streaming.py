import threading
import subprocess

cmd = "ffmpeg -fflags nobuffer -rtsp_transport tcp -i %s -framerate 20 -video_size 720x480 -vcodec libx264 -preset veryfast -maxrate 1984k -bufsize 3968k -vf \"format=yuv420p\" -g 60 -c:a aac -b:a 128k -ar 44100 -f flv %s"
# cmd2 = "ffmpeg -fflags nobuffer -rtsp_transport tcp -i rtsp://admin:Viact123@192.168.92.111/live -framerate 20 -video_size 720x480 -vcodec libx264 -preset veryfast -maxrate 1984k -bufsize 3968k -vf \"format=yuv420p\" -g 60 -c:a aac -b:a 128k -ar 44100 -f flv rtmp://54.254.0.41/live/test2"
# cmd3 = "ffmpeg -fflags nobuffer -rtsp_transport tcp -i rtsp://admin:Viact123@192.168.92.111/live -framerate 20 -video_size 720x480 -vcodec libx264 -preset veryfast -maxrate 1984k -bufsize 3968k -vf \"format=yuv420p\" -g 60 -c:a aac -b:a 128k -ar 44100 -f flv rtmp://54.254.0.41/live/test3"

def thread_function(type, rtsp, rtmp):
    r = cmd%(rtsp, rtmp)
    subprocess.check_output(r, shell=True).decode("utf-8")
   
def new(type, rtsp, rtmp):
    x = threading.Thread(target=thread_function, args=(type, rtsp, rtmp))
    x.daemon = True
    x.start()