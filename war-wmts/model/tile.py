
from db_interface import db_interface


image_map = {
    # basic coverage
    'land,land,land,land': '/var/www/tornado/sprites/summer-tiles/summer-10-15.png',
    'water,water,water,water': '/var/www/tornado/sprites/summer-tiles/summer-17-7.png',
    'forest,forest,forest,forest': '/var/www/tornado/sprites/summer-tiles/summer-7-5.png',
    # forest with land corner
    'forest,forest,forest,land': '/var/www/tornado/sprites/summer-tiles/summer-7-5.png',
    'forest,forest,land,forest': '/var/www/tornado/sprites/summer-tiles/summer-7-5.png',
    'forest,land,forest,forest': '/var/www/tornado/sprites/summer-tiles/summer-7-5.png',
    'land,forest,forest,forest': '/var/www/tornado/sprites/summer-tiles/summer-7-5.png',
    # half forest half land
    'land,land,forest,forest': '/var/www/tornado/sprites/summer-tiles/summer-7-8.png',
    'land,forest,land,forest': '/var/www/tornado/sprites/summer-tiles/summer-7-9.png',
    'forest,forest,land,land': '/var/www/tornado/sprites/summer-tiles/summer-7-11.png',
    'forest,land,forest,land': '/var/www/tornado/sprites/summer-tiles/summer-7-9.png',
    # land with forest corner
    'forest,land,land,land': '/var/www/tornado/sprites/summer-tiles/summer-6-16.png',
    'land,forest,land,land': '/var/www/tornado/sprites/summer-tiles/summer-6-8.png',
    'land,land,forest,land': '/var/www/tornado/sprites/summer-tiles/summer-6-13.png',
    'land,land,land,forest': '/var/www/tornado/sprites/summer-tiles/summer-6-10.png',
    # land with water corner
    'water,land,land,land': '/var/www/tornado/sprites/summer-tiles/summer-11-17.png',
    'land,water,land,land': '/var/www/tornado/sprites/summer-tiles/summer-11-19.png',
    'land,land,water,land': '/var/www/tornado/sprites/summer-tiles/summer-12-5.png',
    'land,land,land,water': '/var/www/tornado/sprites/summer-tiles/summer-12-13.png',
    # half land half water
    'water,water,land,land': '/var/www/tornado/sprites/summer-tiles/summer-12-3.png',
    'land,water,land,water': '/var/www/tornado/sprites/summer-tiles/summer-12-17.png',
    'land,land,water,water': '/var/www/tornado/sprites/summer-tiles/summer-13-2.png',
    'water,land,water,land': '/var/www/tornado/sprites/summer-tiles/summer-12-8.png',
    # water with land corner
    'land,water,water,water': '/var/www/tornado/sprites/summer-tiles/summer-13-8.png',
    'water,land,water,water': '/var/www/tornado/sprites/summer-tiles/summer-13-6.png',
    'water,water,land,water': '/var/www/tornado/sprites/summer-tiles/summer-12-19.png',
    'water,water,water,land': '/var/www/tornado/sprites/summer-tiles/summer-12-12.png',
}



no_data_image_path = '/var/www/tornado/sprites/summer-tiles/summer-1-1.png'


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

    def get_type_matrix(self):
        point_grid_str = ''
        point_grid_str += self.get_point_type(self.left, self.top)
        point_grid_str += ',' + self.get_point_type(self.right, self.top)
        point_grid_str += ',' + self.get_point_type(self.left, self.bottom)
        point_grid_str += ',' + self.get_point_type(self.right, self.bottom)
        return point_grid_str

    def analyze(self):
        point_grid_str = self.get_type_matrix()
        try:
            image_path = image_map[point_grid_str]
        except KeyError:
            image_path = no_data_image_path
        image_data = None
        with open(image_path, 'rb') as f:
            image_data = f.read()
        return image_data

