# README for backend

## Overview

This repository contains the backend for the Energy Monitor Flutter application. It is built with FastAPI, SQLAlchemy, and PostgreSQL. The API provides endpoints for user authentication, energy data ingestion, and energy-saving tips.

## Setup

```bash
# Clone the repo
git clone <repo-url>
cd energymonitor_flutter/backend

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create a .env file (copy from .env.example and adjust values)
cp .env.example .env

# Run database migrations
alembic upgrade head

# Start the server
uvicorn main:app --reload
```

## Docker

```bash
docker build -t energymonitor-backend .
docker run -p 8000:8000 --env-file .env energymonitor-backend
```

## API Endpoints

- `POST /auth/register` – Register a new user.
- `POST /auth/token` – Login and receive a JWT.
- `GET /auth/me` – Get current user info.
- `POST /energy/records` – Submit an energy record.
- `GET /energy/records` – Retrieve energy records for the authenticated user.
- `GET /energy/tips` – Retrieve energy-saving tips.

## Development

- Use `pytest` for tests.
- Use `alembic` for migrations.
- API documentation is available at `/docs` when the server is running.

---
