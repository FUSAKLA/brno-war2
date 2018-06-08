#!/bin/bash

docker exec -it brno-war2_osm2pgsql_1 \
osm2pgsql --create --slim \
    --cache 1000 --number-processes 2 \
    --multi-geometry \
    --database=gis \
    --host=postgis \
    --username=docker \
    --password=docker \
    /home/czech-republic-latest.osm.pbf
