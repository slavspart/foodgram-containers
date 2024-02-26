#!/bin/bash
# Perform database migrations
python manage.py migrate

# Create a superuser
script=$(cat <<EOF
from django.db.utils import IntegrityError
from users.models import User

try:
    User.objects.create_superuser('admin', 'a@a.ad', 'admin')
except IntegrityError:
    print('Superuser with username admin already exists.')
EOF
)

echo "$script" | python manage.py shell

python manage.py collectstatic

python manage.py shell < csv_script.py

# # Start Gunicorn
gunicorn foodgram.wsgi:application --bind 0:8000