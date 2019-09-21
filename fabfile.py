# INSTALLATION
# for python 3.x:   > pip install fabric3
# For python 2.7.x: > pip install fabric

import os
import sys
from fabric.api import (local, run, env, cd, hosts, sudo, put, settings)
from fabric.contrib.files import exists
from fabric.contrib.project import rsync_project
from sys import platform as _platform
from builtins import input

PYTHON_VERSION = sys.version_info
PROJECT_DIR =  os.path.dirname(os.path.abspath(__file__))


@hosts('localhost')
def start():
	global PROJECT_DIR
	local(f'cd { PROJECT_DIR } && docker-compose up')

@hosts('localhost')
def recreate():
	global PROJECT_DIR
	local(f'cd { PROJECT_DIR } && docker-compose down && docker-compose build && docker-compose up')


@hosts('localhost')
def stop():
	try:
		if _platform in ["linux", "linux2", "darwin"]:
			local("docker stop $(docker ps -a -q)")
		elif _platform in ["win32", "win64"]:
			local('FOR /f "tokens=*" %i IN (\'docker ps -a -q\') DO docker stop %i')  # windows CMD
			#  docker stop @(docker ps -aq) # for windows PowerShell only
	except Exception as e:
		print("Error: {0}".format(e))

