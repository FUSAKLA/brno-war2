#!/bin/bash


IPADDRESS=`docker inspect postgis | grep IPAddress | tail -1 | grep -o '[0-9\.]*'`

osm2pgsql --create --slim \
    --cache 1000 --number-processes 2 \
    --multi-geometry \
    --database=gis \
    --host=$IPADDRESS \
    --username=docker \
    --password \
    czech-republic-latest.osm.pbf
