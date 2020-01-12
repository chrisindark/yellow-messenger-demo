release: python manage.py migrate

web: DJANGO_SETTINGS_MODULE=mysite.settings.staging gunicorn mysite.wsgi
