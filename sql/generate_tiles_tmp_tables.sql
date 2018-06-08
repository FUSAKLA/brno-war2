select now();

drop table if exists tmp_points;
create table tmp_points(
	id SERIAL PRIMARY KEY,
	geom GEOMETRY(POINT, 900913)
);
CREATE INDEX tmp_points_gist ON tmp_points USING GIST (geom);

drop table if exists points;
create table points(
	id SERIAL PRIMARY KEY,
	geom GEOMETRY(POINT, 900913),
	type varchar(10) DEFAULT 'land'
);
CREATE INDEX points_gist ON points USING GIST (geom);

drop table if exists tiles;
create table tiles(
	id SERIAL PRIMARY KEY,
	geom geometry(POLYGON, 900913),
	type varchar(100)
);
CREATE INDEX tiles_gist ON tiles USING GIST (geom);

--------------------------------------------------------------------------------

-- takes cca 0.06504150293611197 ms per point
INSERT INTO tmp_points(geom)
	SELECT ST_SetSRID(ST_MakePoint(x, y), 900913) as geom 
	  FROM 
	     generate_series(1835725- 8, 1853894+ 8, 8) as x, 
	     generate_series(6307056- 8, 6317249+ 8, 8) y;
VACUUM ANALYZE tmp_points;

INSERT INTO points(geom,type)
	SELECT geom, type
	  FROM 
	     tmp_points as p,
	     planet_osm_polygon as osm
	  WHERE ST_intersects(osm.way, p.geom);
VACUUM ANALYZE points;

--takes cca 0.09511495443247722 ms per polygon
INSERT INTO tiles(geom)
	SELECT ST_SetSRID(ST_MakePolygon(ST_MakeLine(ARRAY[ST_MakePoint(x,y), ST_MakePoint(x,y+ 8), ST_MakePoint(x+ 8,y+ 8), ST_MakePoint(x+ 8,y), ST_MakePoint(x,y)])), 900913)
  	FROM 
     	generate_series(1835725, 1853894, 8) as x, 
	    generate_series(6307056, 6317249, 8) y;
VACUUM ANALYZE tiles;

-- takes cca 0.10191003866335266 ms per polygon
UPDATE tiles SET type = 
	( 
	SELECT string_agg(p.type, ',' order by p.geom)
	FROM points as p
	WHERE ST_intersects(p.geom, tiles.geom)
	);
VACUUM ANALYZE tiles;


select now();


