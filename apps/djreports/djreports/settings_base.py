# Django settings for hc project.
from os import environ
import os.path

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DIRNAME = os.path.dirname(__file__)
PARENT_DIR = os.path.dirname(os.path.abspath(DIRNAME))

DEBUG = False
TEMPLATE_DEBUG = False

ADMINS = (
    ('Philip Kalinsky', 'pkalinsky@greenlightgo.co'),
)

MANAGERS = ADMINS

INTERNAL_IPS = (
    # If you are working behind a public IP address,
    # add here. E.g.:
    # '123.123.123.123',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'uwsgireports',
        'USER': 'web',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'core', 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
    'less.finders.LessFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3=n06o#=$gj17e^dl$6ff4f-@a#k124ium!mtrebh)ktfic_vl'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    #'core.context_processors.google',
    #'core.context_processors.my_location',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    #'core.middleware.XForwardedForMiddleware',
)

ROOT_URLCONF = 'uwsgireports.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)
GRAPPELLI_ADMIN_TITLE = "uWSGI-fun reports"

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    #'django.contrib.formtools',
    #'django.contrib.humanize',
    #'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    #'django.contrib.webdesign',
    # 3rd Party apps
    'django_extensions',
    #'twitter_bootstrap',
    #'less',
    #'compressor',
    #'sorl.thumbnail',
    # Project specific apps
    "core",
    'debug_toolbar_mongo',
    # south must come last
    'south',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': '',
        'TIMEOUT': 300, # 5 minutes, tune as necessary
        'VERSION': 1,
    }
}

CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'

EMAIL_SUBJECT_PREFIX = 'yo.you [Django] '
DEFAULT_FROM_EMAIL = 'noreply@yo.you'

# Google Analytics UA, e.g. UA-XXXXXXX
GOOGLE_UA = ''

try:
    import geoip_utils
except ImportError:
    pass
else:
    GEOIP_PATH = geoip_utils.where()
    #GEOIP_REQUEST_IP_RESOLVER='geoip_utils.utils.x_forwarded_ip'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# A sample logging configuration.
# Enables console logging at 'DEBUG' level and all higher events
# are logged to django-sentry.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'cities': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}

FIXTURE_DIRS = ("fixtures",)

COMPRESS_OFFLINE = True
COMPRESS_STORAGE = 'compressor.storage.CompressorFileStorage'
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter', 'compressor.filters.cssmin.CSSMinFilter']
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter',]

THUMBNAIL_DUMMY = False
THUMBNAIL_DEBUG = True

LESS_ROOT = STATIC_ROOT
LESS_EXECUTABLE = "/usr/bin/lessc"
