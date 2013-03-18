import os
from rocket_engine import on_appengine, PROJECT_DIR

if on_appengine:
    DATABASES = {
        'default': {
            'ENGINE': 'rocket_engine.db.backends.cloudsql',
            'INSTANCE': 'xando-1-main:main',
            'NAME': 'test',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'development.db'
        }
    }

DEFAULT_FILE_STORAGE = 'rocket_engine.storage.BlobStorage'
DEFAUTL_EMAIL_BACKEND = 'rocket_engine.mail.EmailBackend'

DEBUG = not on_appengine
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'rocket_engine',
    # 'south',

    'core'
)

SITE_ID = 1
