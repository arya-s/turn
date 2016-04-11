import os
import tornado.ioloop
import tornado.web

js_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "js"),

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

def run():
  return tornado.web.Application([
    (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": "./js"}),
    (r"/textures/(.*)", tornado.web.StaticFileHandler, {"path": "./textures"}),
    (r"/", MainHandler),
  ], debug=False)

if __name__ == "__main__":
  app = run()
  app.listen(1337)
  tornado.ioloop.IOLoop.current().start()
