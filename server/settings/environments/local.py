# -*- coding: utf-8 -*-

"""Override any custom settings here."""

import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '))vn+w57l^0o=uxuc&@1u2*g=z*9yu#_%$@7^%j%v_m07a=fdc'                     # 32 bit key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Make it true for the development API
DEV = True

INTERNAL_IPS = [
    '127.0.0.1',
]

GRAPHENE['MIDDLEWARE'] = [
        'graphene_django.debug.DjangoDebugMiddleware',          # debug middleware
    ] + GRAPHENE['MIDDLEWARE']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

HOST_URL = 'xxx'

from datetime import timedelta
# rest JWT configuration
SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'] = timedelta(minutes=120)
SIMPLE_JWT['SIGNING_KEY'] = '4u7x!A%D*G-KaPdSgVkYp3s6v8y/B?E('

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}