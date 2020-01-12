from mysite.settings.common import *
from corsheaders.defaults import default_headers


SECRET_KEY = 'ieq-w-639_lw5e=*5&wjl)nq$k17&cax&sp)2)@cyk$afgo7it'

ALLOWED_HOSTS = (
    'localhost',
    '0.0.0.0',
    '127.0.0.1',
)

DEBUG = True

INSTALLED_APPS += (
    'django_extensions',
    'debug_toolbar',
)

MIDDLEWARE = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
) + MIDDLEWARE

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


STATIC_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, STATIC_PATH))
MEDIA_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, MEDIA_PATH))

CORS_ORIGIN_WHITELIST = ()
CORS_ORIGIN_ALLOW_ALL = True
CORS_EXPOSE_HEADERS = (
    'Access-Control-Allow-Origin',
    'Content-Disposition',
    'Content-Type',
    'Content-Length',
    'App-Version',
)
CORS_ALLOW_HEADERS = default_headers + (
    'Content-Disposition',
)

REDIS_URL = 'redis://127.0.0.1:6379'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL + '/1',
    }
}
