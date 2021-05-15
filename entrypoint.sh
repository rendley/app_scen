#!/bin/bash

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input
#python manage.py createsuperuser
#admin
#admin@example.com
#12345

# For local
#python manage.py runserver 0.0.0.0:5000

exec gunicorn config.wsgi:application -b 0.0.0.0:5000 --reload
