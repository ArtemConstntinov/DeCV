from tornado.web import RequestHandler
from tornado.escape import json_encode, json_decode

class BaseHandler(RequestHandler):
	def read_json(self):
		if self.request.body:
			return json_decode(self.request.body.decode('utf-8'))
		return {}