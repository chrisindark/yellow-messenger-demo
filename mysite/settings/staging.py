from mysite.settings.common import *
from corsheaders.defaults import default_headers


SECRET_KEY = get_env_var('SECRET_KEY')

ALLOWED_HOSTS = (
    'guarded-stream-63902.herokuapp.com',
)

DEBUG = True

INSTALLED_APPS += (
    'django_extensions',
)


if os.environ.get('HEROKU_ENV'):
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=500)
    }
else:
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

REDIS_URL = get_env_var('REDIS_URL')

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
    }
}
