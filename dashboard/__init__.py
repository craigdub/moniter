from pyramid.config import Configurator
from pyramid_jinja2 import renderer_factory
from dashboard.models import get_root

def main(global_config, **settings):
    """ This function returns a WSGI application.
    
    It is usually called by the PasteDeploy framework during 
    ``paster serve``.
    """
    settings = dict(settings)
    settings.setdefault('jinja2.i18n.domain', 'dashboard')

    config = Configurator(root_factory=get_root, settings=settings)
    config.add_translation_dirs('locale/')
    config.include('pyramid_jinja2')

    config.add_static_view('static', 'static')
    config.add_view('dashboard.views.my_view',
                    context='dashboard.models.MyModel', 
                    renderer="mytemplate.jinja2")
    config.scan('dashboard')
    config.add_route('home', '/')
    config.add_route('socket_io', 'socket.io/*remaining')

    return config.make_wsgi_app()
