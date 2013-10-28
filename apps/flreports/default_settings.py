# Global configuration
BROWSER_SECRET_KEY = ''

# Flask-Cache settings
CACHE_TYPE = 'memcached'
CACHE_MEMCACHED_SERVERS = ['127.0.0.1:11211']

# When behind a load balancer, set CANONICAL_NAME to the value contained in
# Host headers (e.g. 'www.example.org')
CANONICAL_NAME = '127.0.0.1'

# When behind a load balancer, set CANONICAL_PORT to the value contained in
# Host headers (normally it will be '80' in production)
CANONICAL_PORT = '5000'

#DB_HOST = '127.0.0.1'
#DB_NAME = 'skeleton'
#DB_PASS = ''
#DB_PORT = '5432'
#DB_SCHEMA = 'skeleton_schema'
#DB_ADMIN = 'skeleton_dba'
#DB_USER = 'skeleton_www'
DEBUG = False
DEBUG_TOOLBAR = False
LISTEN_HOST = '127.0.0.1'
PASSWORD_HASH = ''
SECRET_KEY = ''
SESSION_BYTES = 25
SESSION_COOKIE_NAME = 'flreports_session'
SSL_CERT_FILENAME = ''
SSL_PRIVATE_KEY_FILENAME = ''
TESTING = False
USE_SSL = True

# If users want to pass specific werkzeug options
WERKZEUG_OPTS = {'host': LISTEN_HOST, 'port' : 5000}

# Import user-provided values
try:
    from local_settings import *
except ImportError:
    pass

