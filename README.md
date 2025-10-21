# Django Project — Setup Instructions

This README explains how to set up the project locally on Windows (PowerShell) and common alternatives.

## Prerequisites
- Python 3.8+ installed and on PATH
- pip

## Quick setup (recommended)
1. Open PowerShell in the project root.
2. Create and activate a virtual environment:
    ```powershell
    python -m venv .venv
    ```
3. Install dependencies:
    ```powershell
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
    If `requirements.txt` is missing:
    ```powershell
    pip install django
    ```

4. Configure environment variables:
    - Create a `.env` file or set environment variables required by the project (e.g., `SECRET_KEY`, `DEBUG`, `DATABASE_URL`).
    - Do not commit secrets to version control.

5. Apply migrations and create a superuser:
    ```powershell
    python manage.py migrate
    python manage.py createsuperuser
    ```

6. Collect static files (production or when configured):
    ```powershell
    python manage.py collectstatic --noinput
    ```

7. Run the development server:
    ```powershell
    python manage.py runserver
    ```
    Visit http://127.0.0.1:8000/

## Database notes
- Default: SQLite (no extra config required).
- For PostgreSQL or other DBs: install the appropriate client (e.g., `psycopg2-binary`), update `DATABASES` in settings or set `DATABASE_URL`, then run migrations.

## Tests & linting
- Run tests:
  ```powershell
  python manage.py test
  ```
- Lint/format (if configured):
  ```powershell
  flake8
  black .
  ```

## Docker (optional)
- Build and run with docker-compose if a `docker-compose.yml` exists:
  ```powershell
  docker-compose up --build
  ```

## Common troubleshooting
- "Module not found": ensure virtualenv activated and dependencies installed.
- Permission issues on Windows: run PowerShell as Administrator for port binding or adjust policies for script execution.
- Missing SECRET_KEY: add to `.env` or settings for local dev.

## Useful commands summary
- Activate venv: `.venv\Scripts\Activate.ps1`
- Install deps: `pip install -r requirements.txt`
- Migrate: `python manage.py migrate`
- Create admin: `python manage.py createsuperuser`
- Run server: `python manage.py runserver`
- Tests: `python manage.py test`

Add project-specific notes (custom settings, third-party services, CI) below as needed.