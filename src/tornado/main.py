import os
import sys
import logging
from logging.handlers import TimedRotatingFileHandler

APP_DIR = os.path.dirname(os.path.abspath(__file__))
PROJ_DIR = os.path.dirname(APP_DIR)
sys.path.append(APP_DIR)

from application import run_server

def setup_logging():
	console_handler = logging.StreamHandler()
	console_handler.setLevel(logging.DEBUG)

	file_handler = TimedRotatingFileHandler(
		"/var/log/tornado/tornado.log",
		when="d",
		interval=1,
		backupCount=5,
		encoding=None,
		delay=0
	)

	logging.basicConfig(
		handlers=[file_handler, console_handler],
		datefmt='%m/%d/%Y %I:%M:%S %p',
		level=logging.DEBUG
	)


def main():
	setup_logging()
	run_server()


if __name__ == "__main__":
	main()