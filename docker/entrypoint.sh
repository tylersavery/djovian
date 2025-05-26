#!/bin/bash
set -e

# Apply database migrations
python manage.py migrate

# install tailwind dependencies
echo "Ensuring Tailwind dependencies are installed..."
cd theme/static_src && npm install && cd .. && cd ..

echo "Building JS"
npm install && npm run build

# Collect static files (for prod)
if [ "$DJANGO_ENV" = "production" ]; then
  python manage.py tailwind build
  python manage.py collectstatic --noinput
fi

# Start the appropriate server
if [ "$DJANGO_ENV" != "production" ]; then
  python manage.py runserver 0.0.0.0:8000
fi