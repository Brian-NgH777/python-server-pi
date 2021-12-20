import threading
import subprocess

cmd1 = "ffmpeg -fflags nobuffer -rtsp_transport tcp -i rtsp://admin:Viact123@192.168.92.111/live -framerate 20 -video_size 400x400 -vcodec libx264 -preset veryfast -maxrate 1984k -bufsize 3968k -vf \"format=yuv420p\" -g 60 -c:a aac -b:a 128k -ar 44100 -f flv rtmp://54.254.0.41/live/test1"
cmd2 = "ffmpeg -fflags nobuffer -rtsp_transport tcp -i rtsp://admin:Viact123@192.168.92.111/live -framerate 20 -video_size 400x400 -vcodec libx264 -preset veryfast -maxrate 1984k -bufsize 3968k -vf \"format=yuv420p\" -g 60 -c:a aac -b:a 128k -ar 44100 -f flv rtmp://54.254.0.41/live/test2"
# cmd3 = "ffmpeg -fflags nobuffer -rtsp_transport tcp -i rtsp://admin:Viact123@192.168.92.111/live -framerate 20 -video_size 720x480 -vcodec libx264 -preset veryfast -maxrate 1984k -bufsize 3968k -vf \"format=yuv420p\" -g 60 -c:a aac -b:a 128k -ar 44100 -f flv rtmp://54.254.0.41/live/test3"

def thread_function(thead):
    if thead == 0 :
        subprocess.check_output(cmd1, shell=True).decode("utf-8")
    elif thead == 1 :
        subprocess.check_output(cmd2, shell=True).decode("utf-8")
    # elif thead == 2 :
    #     subprocess.check_output(cmd3, shell=True).decode("utf-8")
    else:
        print("not yet")
        # logging.info("Main    :Not yet")
    # subprocess.check_output("cmd1", shell=True).decode("utf-8")
    print(thead)
    
if __name__ == "__main__":
    for index in range(2):
        x = threading.Thread(target=thread_function, args=(index,), daemon=True)
        # x.daemon = True               
        x.start()
    