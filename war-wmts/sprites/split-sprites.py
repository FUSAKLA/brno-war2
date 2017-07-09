
from PIL import Image
import os
import sys
import shutil

EMPTY_PIXEL = (0, 0, 0, 0)


class TileImage(object):
    def __init__(self, file_path):
        self.image = Image.open(file_path)
        self.width, self.height = self.image.size
        self.name = self.image.filename.split('.')[-2]
        self.dir_name = './{0}-tiles'.format(self.name)

    def _create_tiles_dir(self):
        try:
            shutil.rmtree(self.dir_name)
        except Exception:
            pass
        os.mkdir(self.dir_name)

    def split(self, tile_width, tile_height, v_separator=0, h_separator=0):
        self._create_tiles_dir()

        curr_height = 0
        row = 1

        while curr_height <= self.height:
            curr_width = 0
            column = 1
            while curr_width <= self.width:
                tile = self.image.crop((curr_width, curr_height, curr_width + tile_width, curr_height + tile_height))
                tile.save('./{0}/{1}-{2}-{3}.png'.format(self.dir_name, self.name, row, column))
                curr_width += tile_width + v_separator
                column += 1
            curr_height += tile_height + h_separator
            row += 1


if __name__ == "__main__":
    file_name, tile_width, tile_height, h_separator, v_separator = sys.argv[1:6]
    tiles_image = TileImage(file_name)
    tiles_image.split(int(tile_width), int(tile_height), int(h_separator), int(v_separator))
