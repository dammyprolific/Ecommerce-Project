#!/usr/bin/env bash
set -o errexit

# Step 1: Install dependencies from project root (where pyproject.toml lives)
pip install -r requirements.txt
poetry install

# Step 2: Move into the folder with manage.py
cd Ecommerce

# Step 3: Run Django commands
poetry run python manage.py migrate
poetry run python manage.py collectstatic --no-input

