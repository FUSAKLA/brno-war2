#! /bin/bash

docker stop war-wmts

docker rm war-wmts

docker run  -d --name war-wmts -p 8888:8888 -e "IDX_SCR=index.py" -v /home/brno-war2/war-wmts:/var/www/tornado localhost/war-wmts

sleep 2

docker logs war-wmts
