#!/bin/bash
set -e

if [ -z "$SECRET_KEY" ]; then
  echo "⚠️ SECRET_KEY not found. Generating temporary key..."
  export SECRET_KEY=$(python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
fi

echo "⏳ Waiting for Postgres..."
./wait-for-it.sh db:5432 --timeout=30 --strict -- echo "✅ Postgres is up"


echo "📦 Running database migrations..."
python manage.py migrate

echo "📚 Downloading or updating catalog..."
python manage.py updatecatalog

echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput

echo "🚀 Starting Django development server..."
exec python manage.py runserver 0.0.0.0:8000
