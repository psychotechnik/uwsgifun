from settings_base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG
CRISPY_FAIL_SILENTLY = not DEBUG

COMPRESS_ENABLED = False

INTERNAL_IPS += (
    '127.0.0.1',
)

# Depending on your environment, if you only need to override one database setting, this could be as simple as:
DATABASES['default']['PASSWORD'] = 'web'

# Your time on planet earth will be better spent if you use the exact same db backend as production
# (no sqlite3 if that's not what you use in production).

# Dump all emails to console so we don't risk sending emails
# when using production data
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Uncomment the following to test django_compressor's output in development
# COMPRESS_ENABLED = True

# Uncomment the following lines to enable django-debug-toolbar:
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
   'debug_toolbar_mongo.panel.MongoDebugPanel',
)
DEBUG_TOOLBAR_MONGO_STACKTRACES = False,
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
#INSTALLED_APPS += ('debug_toolbar', )
#MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
#    }
#}
DEBUG_TOOLBAR_CONFIG = { 'INTERCEPT_REDIRECTS' : False, }

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PROJECT_DIR, '../log/uwsgireports.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'request_handler': {
                'class':'django.utils.log.NullHandler',
        },

    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': { # Stop SQL debug from logging to main logger
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}
