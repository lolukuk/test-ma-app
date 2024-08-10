## Media Service API

## Описание

REST API микросервис для приёма, обработки и управления медиафайлами.

## Установка

1. Создайте виртуальное окружение и активируйте его:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

3. Запустите миграции базы данных:

   ```bash
   alembic upgrade head
   ```

4. Запустите сервер:

   ```bash
   uvicorn app.main:app --reload
   ```

## Тестирование

Запустите тесты с помощью pytest