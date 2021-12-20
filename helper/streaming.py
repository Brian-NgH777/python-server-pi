import threading
import subprocess

cmd = "ffmpeg -fflags nobuffer -rtsp_transport tcp -i %s -framerate 20 -video_size 400x400 -vcodec libx264 -preset veryfast -maxrate 1984k -bufsize 3968k -vf \"format=yuv420p\" -g 60 -c:a aac -b:a 128k -ar 44100 -f flv %s"
# cmd2 = "ffmpeg -fflags nobuffer -rtsp_transport tcp -i rtsp://admin:Viact123@192.168.92.111/live -framerate 20 -video_size 720x480 -vcodec libx264 -preset veryfast -maxrate 1984k -bufsize 3968k -vf \"format=yuv420p\" -g 60 -c:a aac -b:a 128k -ar 44100 -f flv rtmp://54.254.0.41/live/test2"
# cmd3 = "ffmpeg -fflags nobuffer -rtsp_transport tcp -i rtsp://admin:Viact123@192.168.92.111/live -framerate 20 -video_size 720x480 -vcodec libx264 -preset veryfast -maxrate 1984k -bufsize 3968k -vf \"format=yuv420p\" -g 60 -c:a aac -b:a 128k -ar 44100 -f flv rtmp://54.254.0.41/live/test3"

def thread_function(rtsp, rtmp):
    try:
        r = cmd%(rtsp, rtmp)
        print("cmd", r)
        subprocess.check_output(r, shell=True).decode("utf-8")
    except subprocess.CalledProcessError as e:
        print(e.output)
        return False
   
def new(rtsp, rtmp):
    x = threading.Thread(target=thread_function, args=(rtsp, rtmp))
    x.daemon = True
    x.start()