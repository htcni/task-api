# Task Backend

## Description

Simple task management written with Django Rest Framework.

## Installation

1. **Clone the repository:**
    ```bash
    https://github.com/htcni/task-api.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd task-api
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Run migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## Configuration
Setup the following .env variables

5. **Environment:**
    ```bash
    SECRET_KEY=
    DEBUG=TRUE
    ALLOWED_HOSTS='localhost'
    DATABASE_URL=
    ```


## Run
```bash
python manage.py runserver
