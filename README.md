# Django Users Project

## Описание

Это проект Django, созданный для выполнения учебного задания. Он включает в себя приложение `users` с моделью пользователя и базовую настройку для работы с базой данных MS SQL Server.

## Установка

1.  **Клонируйте репозиторий (если применимо):**
    ```bash
    git clone <your_repository_url>
    cd <your_project_directory>
    ```

2.  **Создайте и активируйте виртуальное окружение:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # для Windows
    # source venv/bin/activate  # для Linux/macOS
    ```

3.  **Установите зависимости:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Настройте подключение к базе данных MS SQL Server:**
    *   Убедитесь, что у вас установлен MS SQL Server и настроен ODBC драйвер.
    *   Создайте файл `.env` (или `local_settings.py`) в корневой папке проекта и укажите переменные окружения для подключения к базе данных (см. пример ниже).

5.  **Примените миграции:**
    ```bash
    python manage.py migrate
    ```

6.  **Создайте суперпользователя:**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Запустите сервер разработки:**
    ```bash
    python manage.py runserver
    ```

## Настройка базы данных

*   База данных настроена в файле `my_project/settings.py`.
*   Используются переменные окружения для хранения конфиденциальной информации (имя пользователя, пароль, хост базы данных).
*   Пример файла `.env_sample`:

    ```
    DJANGO_SECRET_KEY=your_secret_key
    DJANGO_DEBUG=True
    DJANGO_DATABASE_NAME=your_database_name
    DJANGO_DATABASE_USER=your_database_user
    DJANGO_DATABASE_PASSWORD=your_database_password
    DJANGO_DATABASE_HOST=your_database_host
    DJANGO_DATABASE_PORT=
    DJANGO_DATABASE_OPTIONS_DRIVER=ODBC Driver 17 for SQL Server
    ```

## Зависимости

Проект использует следующие библиотеки, перечисленные в `requirements.txt`:

asgiref==3.8.1 Django==4.2.12 django-mssql-backend==2.8.1 mssql-django==1.5 pyodbc==5.2.0 python-dotenv==1.0.1 pytz==2025.1 sqlparse==0.5.3 tzdata==2025.2