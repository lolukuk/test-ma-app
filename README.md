# Media Service API

## Описание

Media Service API — это RESTful микросервис, разработанный для приема, обработки и управления медиафайлами. Микросервис позволяет загружать файлы через HTTP-запросы, сохранять их на локальный диск, отправлять копии в облачное хранилище, а также сохранять метаданные файлов в базе данных PostgreSQL.

## Технологический стек

- **Язык программирования:** Python
- **Web-фреймворк:** FastAPI
- **База данных:** PostgreSQL
- **ORM:** SQLAlchemy
- **Облачное хранилище:** Используется условное API для демонстрации интеграции

## Установка

### Клонирование репозитория

```bash
git clone https://github.com/lolukuk/media-service-api.git
cd media-service-api
```

### Создание виртуального окружения и установка зависимостей

```bash
python -m venv venv
venv\Scripts\activate     # Для Win

pip install -r requirements.txt
```

### Настройка окружения

Настройте файл `.env` в корневой директории проекта и добавьте следующие переменные:

```plaintext
DATABASE_URL=postgresql+asyncpg://media_user:password@localhost/media_service_db
CLOUD_API_URL=https://example.com/upload
CLOUD_API_KEY=api_key
```

Замените значения `media_user`, `password`, `media_service_db`, `api_key` и `https://example.com/upload` на ваши собственные значения.

### Создание базы данных

Бд создается автоматически при правильных инструкциях прошлого раздела

## Запуск приложения

Для запуска сервера используйте следующую команду:

```bash
uvicorn app.main:app --reload
```

## Использование API

### Загрузка файла

**POST** `/upload/`

**Параметры:**

- `file` (multipart/form-data): Файл для загрузки.

**Ответ:**

- `uid`: Уникальный идентификатор загруженного файла.

### Получение файла по UID

**GET** `/file/{uid}/`

**Параметры:**

- `uid`: Уникальный идентификатор файла.

**Ответ:**

- Файл будет возвращен в ответе на запрос.

## Дополнительные задачи

### Крон для очистки локального диска

Файл `app/crontask.py` содержит пример функции для очистки старых файлов. Вы можете настроить задачу в системе для регулярного выполнения этой функции.

### Тестирование

Тесты находятся в каталоге `tests`.