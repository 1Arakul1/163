#!/usr/bin/env python
import os
import sys
import pyodbc  # Импортируем pyodbc
from dotenv import load_dotenv

def create_database():
    """Попытка создать базу данных MS SQL Server."""
    load_dotenv()

    db_name = "Собачки"  # Имя базы данных, которую мы хотим создать
    db_user = os.getenv("DJANGO_DATABASE_USER")
    db_password = os.getenv("DJANGO_DATABASE_PASSWORD")
    db_host = os.getenv("DJANGO_DATABASE_HOST")
    
    # Проверяем, что все переменные окружения установлены
    if not all([db_user, db_password, db_host]):
        print("Ошибка: Не все необходимые переменные окружения установлены.")
        return

    # Строка подключения для подключения к серверу БЕЗ указания базы данных
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={db_host};UID={db_user};PWD={db_password}'
    
    try:
        # Попытка подключения к серверу
        cnxn = pyodbc.connect(connection_string, autocommit=True)
        cursor = cnxn.cursor()

        # SQL-запрос для создания базы данных
        sql = f"CREATE DATABASE {db_name}"
        cursor.execute(sql)
        print(f"База данных '{db_name}' успешно создана.")
    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        if sqlstate == '42000':  # База данных уже существует
            print(f"База данных '{db_name}' уже существует.")
        else:
            print(f"Ошибка при создании базы данных: {ex}")
    finally:
        if cnxn:
            cnxn.close()


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings') # Исправлено имя проекта
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    load_dotenv()  # Загружаем переменные окружения
    create_database()  # Пытаемся создать базу данных
    main()