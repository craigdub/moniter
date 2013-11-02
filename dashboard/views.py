from pyramid.i18n import TranslationStringFactory
import psutil
from pyramid.response import Response
from pyramid.view import view_config
from socketio.namespace import BaseNamespace
from socketio import socketio_manage
import json
import pprint
import pdb
import urllib2
from gevent import sleep
import time

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

    def on_page_load(self, j):
        self.spawn(self.page_load, j)

    def page_load(self, j):
        pdb.set_trace()
        while self.socket.state == self.socket.STATE_CONNECTED:
            nf = urllib2.urlopen(j['url'])
            start = time.time()
            page = nf.read()
            end = time.time()
            nf.close()

            load_time = end - start

            self.emit('page_load', {'url': j['url'], 'load_time': load_time})

            sleep(5)


@view_config(route_name='socket_io')
def socketio_service(request):
    retval = socketio_manage(request.environ,
        {
        '': View
        }, request=request 
        )

    return Response('')