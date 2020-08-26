Useful commands
===========================

## Setup project and venv
```bash
pyenv virtualenv 3.7.7 django-v3-crm
pyenv shell django-v3-crm
pip install django
pip install django-filter
django-admin startproject crm
mv crm django-v3-crm
cd django-v3-crm
```

## Django app
```bash
python manage.py startapp accounts
python manage.py migrate
python manage.py createsuperuser
```

## Django migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
