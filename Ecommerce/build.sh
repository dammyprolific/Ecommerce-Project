#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
poetry install

cd Ecommerce

python manage.py migrate
python manage.py collectstatic --no-input
