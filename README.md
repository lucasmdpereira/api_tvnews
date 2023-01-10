# How to start

## Install some Python and Django
Install python3 

```Bash
sudo apt install python3
```

Confirm if python3 is installed

```Bash
python3 --version
```

Install Django

```Bash
python3 -m pip install Django
```

Confirm if Django is installed

```Bash
python3 -m django --version
```

## Start a Django Project

To start a Django project I recomend: 

```Bash
django-admin startproject setup
```
Django will create a setup/setup folder. You can rename the first one, like myproject/setup

Run a server to test (ignore all the errors)

```Bash
python3 manage.py runserver
```

### Venv

Virtual ENViroment is recomended, but you can skip this

```Bash
python3 -m venv venv
```

To open Virtual Enviroment:

```Bash
source venv/bin/activate
```

To deactivate just tap:

```Bash
deactivate
```

## Start an app

Each application you write in Django consists of a Python package that follows a certain convention. To create a package:

```Bash
python3 manage.py startapp myapp
```

## .env

```Bash
pip install python-dotenv
```

Add to settings.py:

```Python
from pathlib import Path, os
from dotenv import load_dotenv
load_dotenv()
```

Copy the SECRET_KEY to .env and put in settings.py

```Python
SECRET_KEY = str(os.getenv('SECRET_KEY'))
```

## Installed_apps

Everytime tha an app is created, you must edit settings.py and put this app
on INSTALLED_APPS

Example:
```Python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tvs'
]
```

I recomend to comment 'django.middleware.csrf.CsrfViewMiddleware' in MIDDLEWARE
for prevent cors erros during development



















