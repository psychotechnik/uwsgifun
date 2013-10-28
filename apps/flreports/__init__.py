import json, os, re, sys

from flask import Flask
#import pytz  # NOTE: Import gae.pytz before Babel!!!
from flask.ext.babel import Babel
#from flask.ext.cache import Cache
from flask.ext.mongoengine import MongoEngine
from flask_debugtoolbar import DebugToolbarExtension
from repoze.browserid.middleware import BrowserIdMiddleware
from werkzeug.contrib.securecookie import SecureCookie

from . import filters

__all__ = ['create_app', 'db']

# A list of app modules and their prefixes. Each APP entry must contain a
# 'name', the remaining arguments are optional. An optional 'models': False
# argument can be given to disable loading models for a given module.
MODULES = [
#   {'name': 'foo',  'url_prefix': '/admin' },
#    {'name': 'aaa',  'url_prefix': '/'      },
    {'name': 'srvstats', 'url_prefix': '/'      },
#    {'name': 'mod1', 'url_prefix': '/'      },
#    {'name': 'mod2', 'url_prefix': '/mod2'  },
#    {'name': 'mod3', 'url_prefix': '/mod3'  },
]


def create_app(name = __name__):
    app = Flask(__name__, static_path='/static')
    load_config(app)
    babel.init_app(app)
    #cache.init_app(app)

    db.init_app(app)
    filters.init_app(app)
    register_local_modules(app)

    app.wsgi_app = ProxyFixupHelper(app.wsgi_app)

    # Enable the DebugToolbar
    if app.config['DEBUG_TOOLBAR']:
        toolbar = DebugToolbarExtension(app)

    # Always attempt to set a BrowserId. At some point this will get used,
    # but let's start setting it now.
    app.wsgi_app = BrowserIdMiddleware(
        app.wsgi_app, secret_key=app.config['BROWSER_SECRET_KEY'],
        cookie_name='b', cookie_path='/',
        cookie_domain=None, cookie_lifetime=86400 * 365 * 10,
        cookie_secure=None, vary=())

    return app


def load_config(app):
    app.config.from_object(__name__)
    app.config.from_object('default_settings')
    app.config.from_envvar('SKELETON_SETTINGS', silent=True)


# Load the local modules
def load_module_models(app, module):
    if 'models' in module and module['models'] == False:
        return

    name = module['name']
    if app.config['DEBUG']:
        print '[MODEL] Loading db model %s' % (name)
    model_name = '%s.models' % (name)
    try:
        mod = __import__(model_name, globals(), locals(), [], -1)
    except ImportError as e:
        if re.match(r'No module named ', e.message) == None:
            print '[MODEL] Unable to load the model for %s: %s' % (model_name, e.message)
        else:
            print '[MODEL] Other(%s): %s' % (model_name, e.message)
        return False
    return True


def register_local_modules(app):
    cur = os.path.abspath(__file__)
    sys.path.append(os.path.dirname(cur) + '/modules')
    for m in MODULES:
        mod_name = '%s.views' % m['name']
        try:
            views = __import__(mod_name, globals(), locals(), [], -1)
        except ImportError:
            load_module_models(app, m)
        else:
            url_prefix = None
            if 'url_prefix' in m:
                url_prefix = m['url_prefix']

            if app.config['DEBUG']:
                print '[VIEW ] Mapping views in %s to prefix: %s' % (mod_name, url_prefix)

                # Automatically map '/' to None to prevent modules from
                # stepping on one another.
            if url_prefix == '/':
                url_prefix = None
            load_module_models(app, m)
            app.register_module(views.module, url_prefix=url_prefix)


# Seeing 127.0.0.1 is almost never correct, promise.  We're proxied 99.9% of
# the time behind a load balancer or proxying webserver. Pull the right IP
# address from the correct HTTP header. In my hosting environments, I inject
# X-Real-IP as the HTTP header of choice instead of appending to
# X-Forwarded-For. Mixing and matching HTTP headers used by a client's proxy
# infrastructure and the server's infrastructure is almost always a bad idea.
class ProxyFixupHelper(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # Only perform this fixup if the current remote host is localhost.
        if environ['REMOTE_ADDR'] == '127.0.0.1':
            host = environ.get('HTTP_X_REAL_IP', False)
            if host:
                environ['REMOTE_ADDR'] = host
        return self.app(environ, start_response)

# Flask Extensions
babel = Babel()

#cache = Cache()

db = MongoEngine()


# Heed SecureCookie.rst's warning and use json instead of pickle for
# serialization.
class JSONSecureCookie(SecureCookie):
    serialization_method = json
