ps aux | grep ffmpeg  | awk '{print $2}' | xargs kill -9