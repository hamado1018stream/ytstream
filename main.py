import os

os.system('ffmpeg -stream_loop -1 -re -i lofi.gif -stream_loop -1 -re -i music.mp3 -vf "scale=854:480" -c:v libx264 -pix_fmt yuv420p -b:v 800k -maxrate 800k -bufsize 1600k -preset veryfast -r 30 -g 60 -crf 23 -c:a aac -b:a 64k -ar 44100 -f flv -fflags nobuffer rtmp://a.rtmp.youtube.com/live2/8qu9-xmf9-b5du-u9g4-b92t')
