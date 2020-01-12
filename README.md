# yellow-messenger-demo


Prerequisites:

* Python 3.7

Checkout the repo:
```bash
git clone https://github.com/chrisindark/yellow-messenger-demo.git
```

Create virtualenv:
```bash
virtualenv env
source env/bin/activate
```

Install requirements:
```bash
pip install -r requirements.txt
```

Migrate the database:
```bash
python manage.py migrate
```

Create a superuser:
```bash
python manage.py createsuperuser
```

Collect static files from each of your applications into a single location:
```bash
python manage.py collectstatic
```

Start the development http server
```bash
python manage.py runserver --settings=mysite.settings.development
```

Open your web browser and go to `127.0.0.1:8000/tinyurls`


# Heroku App

The heroku app uses heroku postgres as database and heroku redis as a caching service.
Link to the app:
```bash
https://guarded-stream-63902.herokuapp.com/api/tinyurls/
```

Url for redirection:
```bash
https://guarded-stream-63902.herokuapp.com/<tiny_url_id>/
```
