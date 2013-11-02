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


class View(BaseNamespace):
    """Dashboard View
    """
    def on_init(self):
        self.spawn(self.second_cpu)
        self.spawn(self.second_network)

    def second_cpu(self):
        while self.socket.state == self.socket.STATE_CONNECTED:
            stats = psutil.cpu_percent() 
            self.emit('second_cpu', stats)
            sleep(1)

    def second_network(self):
        while self.socket.state == self.socket.STATE_CONNECTED:
            stats = psutil.network_io_counters(pernic=False)
            self.emit('second_net_bandwidth', json.dumps(stats._asdict()))
            sleep(1)


@view_config(route_name='socket_io')
def socketio_service(request):
    retval = socketio_manage(request.environ,
        {
        '': View,
        }, request=request 
        )

    return Response('')