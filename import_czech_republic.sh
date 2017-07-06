#!/bin/bash


osm2pgsql --create --slim \
    --cache 1000 --number-processes 2 \
    --multi-geometry \
    --database=gis \
    --host=localhost \
    --username=docker \
    --password \
    czech-republic-latest.osm.pbf
