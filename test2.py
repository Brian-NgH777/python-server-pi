import threading
import subprocess
import os

try:
    from subprocess import DEVNULL # py3k
except ImportError:
    import os
    DEVNULL = open(os.devnull, 'wb')

cmd1 = "ffmpeg -fflags nobuffer -rtsp_transport tcp -i rtsp://admin:Viact123@192.168.92.111/live -framerate 20 -video_size 400x400 -vcodec libx264 -preset veryfast -maxrate 1984k -bufsize 3968k -vf \"format=yuv420p\" -g 60 -c:a aac -b:a 128k -ar 44100 -f flv rtmp://54.254.0.41/live/test1 -nostdin -nostats </dev /null>/dev/null 2>&1 &"
cmd2 = "ffmpeg -fflags nobuffer -rtsp_transport tcp -i rtsp://admin:Viact123@192.168.92.111/live -framerate 20 -video_size 400x400 -vcodec libx264 -preset veryfast -maxrate 1984k -bufsize 3968k -vf \"format=yuv420p\" -g 60 -c:a aac -b:a 128k -ar 44100 -f flv rtmp://54.254.0.41/live/test2 -nostdin -nostats </dev /null>/dev/null 2>&1 &"
# cmd3 = "ffmpeg -fflags nobuffer -rtsp_transport tcp -i rtsp://admin:Viact123@192.168.92.111/live -framerate 20 -video_size 720x480 -vcodec libx264 -preset veryfast -maxrate 1984k -bufsize 3968k -vf \"format=yuv420p\" -g 60 -c:a aac -b:a 128k -ar 44100 -f flv rtmp://54.254.0.41/live/test3"

def thread_function(thead):
    if thead == 0 :
        #Popen(cmd1, shell=True, stdout=DEVNULL)
        # os.system()
        subprocess.call("ffmpeg -fflags nobuffer -rtsp_transport tcp -i rtsp://admin:Viact123@192.168.92.111/live -framerate 20 -video_size 400x400 -vcodec libx264 -preset veryfast -maxrate 1984k -bufsize 3968k -vf \"format=yuv420p\" -g 60 -c:a aac -b:a 128k -ar 44100 -f flv rtmp://54.254.0.41/live/test1", shell=True, stdout=DEVNULL)
    elif thead == 1 :
        # Popen(cmd2, shell=True, stdout=DEVNULL)
        #  os.spawnl(os.P_DETACH, cmd2)
        subprocess.call("ffmpeg -fflags nobuffer -rtsp_transport tcp -i rtsp://admin:Viact123@192.168.92.111/live -framerate 20 -video_size 400x400 -vcodec libx264 -preset veryfast -maxrate 1984k -bufsize 3968k -vf \"format=yuv420p\" -g 60 -c:a aac -b:a 128k -ar 44100 -f flv rtmp://54.254.0.41/live/test2 &> /dev/null", shell=True, stdout=DEVNULL)
        # os.system(cmd2)
    # elif thead == 2 :
    #     subprocess.check_output(cmd3, shell=True).decode("utf-8")
    else:
        print("not yet")
        # logging.info("Main    :Not yet")
    # subprocess.check_output("cmd1", shell=True).decode("utf-8")
    print(thead)
    
if __name__ == "__main__":
    # subprocess.Popen(cmd1, stderr = subprocess.STDOUT, stdout = subprocess.PIPE)
    for index in range(2):
        x = threading.Thread(target=thread_function, args=(index,))
        x.start()
    