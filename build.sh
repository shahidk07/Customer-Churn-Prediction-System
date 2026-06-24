#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Run migrations
python churn_project/manage.py migrate

# Collect static files
python churn_project/manage.py collectstatic --no-input
