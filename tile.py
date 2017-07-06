
import db_interface
from PIL import Image

image_map = {
    'land,land,land,land': './sprites/summer-tiles/summer-6-8.png',
    'water,water,forest,water': './sprites/summer-tiles/summer-13-1.png',

}


class Tile(object):
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top
        self.width = abs(self.right - self.left)
        self.height = abs(self.top - self.bottom)

    @staticmethod
    def get_point_type(x, y):
        point_type = db_interface.get_point_type(x, y)
        if not point_type:
            point_type = 'land'
        return point_type

    def get_type_matrix(self, horizontal_division, vertical_division):
        vertical_step = self.width / (vertical_division + 1)
        horizontal_step = self.height / (horizontal_division + 1)
        point_grid_str = ''
        point_grid_str += self.get_point_type(self.top, self.left)
        point_grid_str += ',' + self.get_point_type(self.top, self.right)
        point_grid_str += ',' + self.get_point_type(self.bottom, self.left)
        point_grid_str += ',' + self.get_point_type(self.bottom, self.right)
        return point_grid_str

    def analyze(self, horizontal_division=1, vertical_division=1):
        point_grid_str = self.get_type_matrix(horizontal_division, vertical_division)
        Image.open(image_map[point_grid_str]).show()


if __name__ == "__main__":
    # t = Tile(6316923.47903259, 1836642.27367164, 6317004.59673633, 1836723.39137537)
    t = Tile( 6317296.28974549, 1835385.05238056,  6317359.93290215, 1835448.69553723)
    t.analyze()