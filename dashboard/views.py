from pyramid.i18n import TranslationStringFactory
import psutil
from pyramid.response import Response
from pyramid.view import view_config
from socketio.namespace import BaseNamespace
from socketio import socketio_manage
import json
import pprint
import pdb
from gevent import sleep

_ = TranslationStringFactory('dashboard')

@view_config(route_name='home', renderer="mytemplate.jinja2")
def my_view(request):
	return {'project': 'dashboard'}

class CPU_Stats(BaseNamespace):
	"""Socket CPU Namespace Goodness
	"""
	def on_init(self):
		self.spawn(self.second_cpu)

	def second_cpu(self):
		while self.socket.state == self.socket.STATE_CONNECTED:
			stat_cpu = psutil.cpu_percent()	
			self.emit('second_cpu', stat_cpu)
			print stat_cpu
			sleep(1)

@view_config(route_name='socket_io')
def socketio_service(request):
	retval = socketio_manage(request.environ,
		{
		'': CPU_Stats
		}, request=request 
		)

	return Response('')