import tornado.ioloop
import tornado.web
import tornado.httpserver
from handlers.capabilities import CapabilitiesHandler
from handlers.tiles import TilesHandler
from handlers.map import MapHandler
from logger import make_logger


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world, YESSSS?!")




def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/map", MapHandler),
        (r"/wmts/layer/([a-zA-Z0-9\-\_]+)/wmts-capabilities", CapabilitiesHandler),
        (r"/tiles/([a-zA-Z0-9\-\_]+)/([a-zA-Z0-9\-\_]+)/([a-zA-Z0-9\-\_]+)/([a-zA-Z0-9\-\_]+)", TilesHandler),
    ],
        debug=True
    )


if __name__ == "__main__":
    logger = make_logger('stdout')
    logger.info('war-wmts started...')
    logger.propagate = False

    app = make_app()
    app.listen(8888)



    tornado.ioloop.IOLoop.current().start()
