
# Setup Guide

Clone the project

```bash
  git clone https://bitbucket.org/django-recipes/backend.git
```

Go to the project directory

```bash
  cd backend
```

create virtual environment

```bash
  python -m venv venv
```

Go to our django project folder
```bash
  cd ads_system
```

Install packages
```bash
  pip install -r requirements.txt
```

Create .env file (template .env.example) and paste generated key in .env file for SECRET_KEY using the above code from terminal.
```bash
  python manage.py shell
  from django.core.management.utils import get_random_secret_key
  print(get_random_secret_key)
```

Set USE_SQLITE = True if you don't want to use postgres or other db in .env file

Migrate

```bash
  python manage.py migrate
```

Create super user

```bash
  python manage.py createsuperuser
  1) enter username e.g admin
  2) enter email or leave blank
  3) enter password
```

Start server

```bash
  python manage.py runserver
```

Login with the credentials cretaed above
```bash
  http://127.0.0.1:8000/admin
```

APIs
```bash
  http://127.0.0.1:8000/api
```