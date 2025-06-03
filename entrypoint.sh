#!/bin/bash

set -e 

echo "📦 Running migrations..."
python manage.py migrate

echo "📚 Updating catalog (may take a few minutes)..."
python manage.py updatecatalog

echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput

echo "🚀 Starting server..."
exec "$@"
