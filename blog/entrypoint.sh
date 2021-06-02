#! /bin/bash

python manage.py makemigrations --no-input


python manage.py migrate


python manage.py collectstatic --no-input


exec gunicorn blog.wsgi:application -b 0.0.0.0:8000 --reload

