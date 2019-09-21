import os
from tornado.web import Application
from tornado.platform import asyncio
from tornado.log import enable_pretty_logging
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import (define, options)
from urls import handlers

class DeCvApplication(Application):
	def __init__(self) -> None:
		try:
			DEBUG = bool(int(os.getenv('DEBUG', 0)))
		except ValueError as e:
			print(f"Wrong value in .env file: {e}")
			print("DEBUG set to: False")
			DEBUG = False

		settings = dict(
			# template_path = os.path.join(APP_DIR, "templates"),
			# static_path = os.path.join(APP_DIR, "static"),
			websocket_ping_interval = 15,
			debug = DEBUG,
		)
		super().__init__(handlers, **settings)


def run_server() -> None:
	define("port", default=8888, help="Run on the given port", type=int)

	asyncio.AsyncIOMainLoop().install()
	io_loop = IOLoop.current()
	enable_pretty_logging()

	app = DeCvApplication()
	max_buffer_size = 2 * 1024**3 # 2GB
	http_server = HTTPServer(
		app,
		max_buffer_size = max_buffer_size,
	)
	http_server.listen(options.port)
	io_loop.start()