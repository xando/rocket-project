from rocket_engine import on_appengine

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

DEBUG = not on_appengine
TEMPLATE_DEBUG = DEBUG


ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    'templates'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'rocket_engine',

    'test'
)

SITE_ID = 1
