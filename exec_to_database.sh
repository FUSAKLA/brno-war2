#!/bin/bash

docker exec -it brno-war2_postgis_1 \
   psql -d gis \
        -h localhost \
        -U docker \
        -W docker
