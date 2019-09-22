import os
import json
from .base_handler import BaseHandler
from typing import Union, Optional, List, Dict, Any, Callable

class DataHandler(BaseHandler):
	async def get(self, url, id) -> None:
		if url and id:
			file_path = os.path.join('/data', f"{ url }", f"{ id }.json") # script injection risk ...
			print(file_path)
			if os.path.isfile(file_path):
				with open(file_path, "r") as json_file:
					json_data = json.load(json_file)
					self.write(json_data)
		self.finish()