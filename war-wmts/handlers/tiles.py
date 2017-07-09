
import tornado.web
from model import tile
import logging


logger = logging.getLogger('war-wmts')

min_x = -20037508.3428
max_y = 20037508.3428

tile_height = 32
tile_width = 32

scale = 1066.364791924892

pixel_size = 0.00028



class TilesHandler(tornado.web.RequestHandler):
    #@tornado.web.asynchronous
    def get(self, tile_matrix_set, tile_matrix, tile_col, tile_row):
        tile_top = max_y - ((int(tile_row)+1) * scale * tile_height * pixel_size)
        tile_left = min_x + ((int(tile_col)+1) * scale * tile_width * pixel_size)
        tile_bottom = tile_top - (scale * tile_height * pixel_size)
        tile_right = tile_left + (scale * tile_width * pixel_size)
        # t = tile.Tile(6317296.28974549, 1835385.05238056, 6317359.93290215, 1835448.69553723)
        logger.debug("%s, %s", tile_left, tile_top)
        t = tile.Tile(tile_left, tile_bottom, tile_right, tile_top)
        image_data = t.analyze()
        self.set_header('Content-Type', 'image/png')
        self.write(image_data)
