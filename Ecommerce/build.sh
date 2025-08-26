#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

cd Ecommerce

python manage.py migrate
python manage.py collectstatic --no-input

