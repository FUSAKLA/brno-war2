
import tornado.web


CAPABILITIES_PATH_PATTERN = "/var/www/tornado/wmts_capabilities/{layer_name}.xml"


class CapabilitiesHandler(tornado.web.RequestHandler):
    def get(self, layer):
        path = CAPABILITIES_PATH_PATTERN.format(layer_name=layer)
        self.set_header('Content-Type', '')
        try:
            self.render(path)
        except FileNotFoundError:
            self.clear()
            self.set_status(404)
            self.write("<html><body>Error 404</br>Layer {layer} not found</body></html>".format(layer=layer))
