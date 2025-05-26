# syntax=docker/dockerfile:1

FROM python:3.12-slim

# Set environment vars
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-openbsd \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs

# Create work dir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

ARG DJANGO_ENV ADMIN_THEME_EDITABLE ALLOWED_HOSTS DATABASE_URL DEBUG SECRET_KEY \
    AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_STORAGE_BUCKET_NAME AWS_DEFAULT_REGION REDIS_URL \
    USE_S3_FOR_STATIC_FILES FRONTEND_BASE_URL PROCESS_TASKS_ASYNC BROKER_URL \
    EMAIL_HOST EMAIL_HOST_USER EMAIL_HOST_PASSWORD EMAIL_PORT EMAIL_USE_TLS DEFAULT_FROM_EMAIL \
    STRIPE_PUBLISHABLE_KEY STRIPE_SECRET_KEY STRIPE_WEBHOOK_SECRET 


# Collect static (prod only)
RUN mkdir -p /app/static

# For ensuring postgres is ready
COPY ./docker/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Tailwind
WORKDIR /app/theme/static_src
RUN npm install

WORKDIR /app

# Gunicorn entrypoint
COPY ./docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]