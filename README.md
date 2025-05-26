# 🎬 Djovian

A full-stack Django starter project.

---

## 🚀 Stack

- **Backend:** Django + HTMX
- **Frontend Styling:** TailwindCSS + DaisyUI
- **Payments:** Stripe
- **Dev Tools:** Docker, Docker Compose, Makefile
- **Async Tasks:** Celery + Redis
- **DB:** PostgreSQL
- **Caching/Queues:** Redis

---

## ⚙️ Local Setup

### 1. Clone the repo

```bash
git clone git@github.com:tylersavery/djovian.git
cd djovian
```

### 2. Create `.env`

Copy the example and tweak values if needed:

```bash
cp .env.example .env
```

And update with your local secrets.


### 3. Build & run services

```bash
make build
make up
```

### 4. Run initial setup

```bash
make migrate
make createsuperuser
```

Then visit: [http://localhost:8000/admin](http://localhost:8000/admin)

---

## 🛠️ Common Dev Tasks

| Task                        | Command                  |
|----------------------------|--------------------------|
| Run dev server             | `make dev`               |
| Create new migrations      | `make makemigrations`    |
| Apply DB migrations        | `make migrate`           |
| Open Django shell          | `make shell`             |
| Start Celery worker        | `make celery`            |
| View logs                  | `make logs`              |
| View Celery logs only      | `make logs-celery`       |
| Run tests                  | `make test`              |

---

## 🐰 Background Tasks

The platform uses **Celery** + **Redis** for async jobs.

Start the worker:
```bash
make celery
```

---

## 🧱 Services

| Service    | URL                          |
|------------|------------------------------|
| Web        | http://localhost:8000        |
| Admin      | http://localhost:8000/admin  |
| Postgres   | `localhost:5432`             |
| Redis      | `localhost:6379`             |


---

## 📦 Deployment

In production:
- Set `DJANGO_ENV=production`
- Gunicorn will start automatically
- Use Nginx to reverse proxy to the container
- Make sure static files are served via volume or CDN

---
