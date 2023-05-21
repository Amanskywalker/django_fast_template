import os

from datetime import timedelta

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "))vn+w57l^0o=atfw&@1u2*g=z*9yu#_%$@7^%j%v_m07a=fdc"

# Application Code
APPLICATION_CODE = "TATO"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Make it true for the development API
DEV = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASE_NAME = "ci"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}