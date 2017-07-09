import psycopg2




def get_point_type(x, y):
    conn = psycopg2.connect("dbname=gis user=docker password=docker host=172.17.0.1 port=5432")
    cur = conn.cursor()
    cur.execute(
        "SELECT type FROM planet_osm_polygon WHERE st_intersects(way, st_setsrid(st_point(%s, %s),900913))",
        (x, y)
    )
    res = cur.fetchone()
    if res:
        point_type = res[0]
    else:
        point_type = None
    cur.close()
    conn.close()
    return point_type
