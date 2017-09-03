from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x0&8_mrx7qkn3i3e6sn_NOT_THE_REAL_KEY_mkkwi18ad(m*k'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Google smtp settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'magicalsmilesnl@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
# EMAIL_TIMEOUT is using default


# Logging setup from django docs that outputs to console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}


try:
    from .local import *
except ImportError:
    pass
