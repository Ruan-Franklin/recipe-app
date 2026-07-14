# Recipe API Project

A robust backend API for managing recipes, built with **Django** and **Django REST Framework (DRF)**, with a containerized development workflow using **Docker**, **docker-compose**, and optional **Dev Containers**.

---

## 🚀 Features

- User authentication and authorization
- Create, read, update, and delete recipes
- Upload and manage recipe images
- Tagging and ingredient organization
- Filter recipes by tags, ingredients, and other query params
- API-first architecture for mobile/web frontend integration
- Containerized development and deployment-ready structure

---

## 🧱 Tech Stack

- **Python**
- **Django**
- **Django REST Framework**
- **PostgreSQL** (typical setup with Docker)
- **Docker / docker-compose**
- **GitHub Actions** (if configured for CI)

---

## 📁 Project Structure (Typical)

```text
recipe-app/
├── app/
├── app/core/
├── app/recipe/
├── app/user/
├── requirements.txt
├── requirements.dev.txt
├── docker-compose.yml
├── Dockerfile
└── README.md
```

> Note: Exact structure may vary slightly depending on your current implementation.

---

## ⚙️ Getting Started (Docker Compose)

### 1) Clone the repository

```bash
git clone https://github.com/Ruan-Franklin/recipe-app.git
cd recipe-app
```

### 2) Create environment file

Create a `.env` file in the project root (adjust values as needed):

```env
DJANGO_SECRET_KEY=changeme-super-secret-key
DJANGO_DEBUG=1
POSTGRES_DB=devdb
POSTGRES_USER=devuser
POSTGRES_PASSWORD=changeme
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

### 3) Build and start services

```bash
docker-compose build
docker-compose up
```

Or detached mode:

```bash
docker-compose up -d
```

### 4) Run database migrations

```bash
docker-compose run --rm app sh -c "python manage.py migrate"
```

### 5) Create superuser (optional)

```bash
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

### 6) Access the API

- API base URL: `http://127.0.0.1:8000/`
- Admin panel: `http://127.0.0.1:8000/admin/`

---

## 🧪 Running Tests

Run tests in the app container:

```bash
docker-compose run --rm app sh -c "python manage.py test"
```

If your project uses `pytest`, you can use:

```bash
docker-compose run --rm app sh -c "pytest"
```

---

## 🧹 Linting / Formatting

If configured, run linting like:

```bash
docker-compose run --rm app sh -c "flake8"
```

or with `black`/`isort`:

```bash
docker-compose run --rm app sh -c "black . && isort ."
```

---

## 🧭 Development with Dev Container (Optional)

If you use VS Code Dev Containers:

1. Install:
   - **Docker**
   - **VS Code**
   - **Dev Containers** extension
2. Open the repository in VS Code
3. Run: **“Dev Containers: Reopen in Container”**
4. Once the container is ready:
   - Run migrations
   - Start server/tests from integrated terminal

If `.devcontainer/` is not yet included, standard `docker-compose` workflow above is recommended.

---

## 🔐 Authentication

This API is designed to support authenticated access for protected endpoints.
Typical auth approaches in DRF projects include:

- Token Authentication
- JWT Authentication

Check your endpoint docs and settings for the exact implementation used in this repository.

---

## 📌 Common Commands

```bash
# Build containers
docker-compose build

# Start services
docker-compose up

# Stop services
docker-compose down

# Run migrations
docker-compose run --rm app sh -c "python manage.py migrate"

# Create admin user
docker-compose run --rm app sh -c "python manage.py createsuperuser"

# Run tests
docker-compose run --rm app sh -c "python manage.py test"
```
