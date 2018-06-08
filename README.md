# brno-war2
Map of Brno city in Warcraft 2 style




To get data run:

```bash
download_czech_republic.sh
docker-compose up -d
import_czech_republic.sh
exec_to_database.sh
```


http://wiki.openstreetmap.org/wiki/Key:landuse
http://wiki.openstreetmap.org/wiki/Key:natural

# forest
landuse in ('forest')

# water
planet_osm_polygon.natural in ('water', 'bay')

# rocks
planet_osm_polygon.natural in ('bare_rock', 'scree', 'cliff', 'rock', 'stone')
