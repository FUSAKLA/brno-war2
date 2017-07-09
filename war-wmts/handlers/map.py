
import tornado.web

MAP_PATH = "/var/www/tornado/map.html"


class MapHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            self.render(MAP_PATH)
        except FileNotFoundError:
            self.clear()
            self.set_status(404)
            self.finish("<html><body>Error 404</br>Map not found</body></html>")
