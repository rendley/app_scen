#!/bin/bash

python manage.py makemigrations --no-input
python manage.py migrate --no-input


# For local
#python manage.py runserver 0.0.0.0:5000

exec gunicorn config.wsgi:application -b 0.0.0.0:5000 --reload
