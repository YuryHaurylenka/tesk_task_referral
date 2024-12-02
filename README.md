# Referral System

# EN

## Description

This is a referral system project built with Django and Django Rest Framework (DRF). The system allows users to register via a simulated code sending process (in reality, the code is checked through the database), as well as generate and activate invite codes.

The project includes:

- Phone number-based authentication (simulation)
- Invite code generation
- API for interacting with the functionality
- User interface based on Django Templates
- Deployment on Heroku (available at [Heroku App](https://test-task-referral-system-92eb6c8cfef3.herokuapp.com/))

## Installation

### Requirements

- Python 3.10 or higher
- PostgreSQL
- Docker

### Installing Dependencies

1. Clone the repository:

   ```bash
   git clone https://github.com/YuryHaurylenka/test_task_referral.git
   cd test_task_referral
   ```

2. Create a .env file in the root of the project and add the following variables:
   ```bash
   SECRET_KEY='your_secret_key'
   
   DEBUG=True
   ALLOWED_HOSTS='localhost, 127.0.0.1,'
   
   API_BASE_URL=http://127.0.0.1:8000/api
   
   # credentials 
   POSTGRES_DB=referral_system
   POSTGRES_USER=referral_user
   POSTGRES_PASSWORD=securepassword
   POSTGRES_HOST=db
   POSTGRES_PORT=5432
   ```

## Running the Project

1. Build and start the containers:
   ```bash
   docker-compose build
   docker-compose up
   ```

2. Apply database migrations:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

3. Once the containers are running, the project will be available at http://127.0.0.1:8000

## Application Structure

### API Endpoints

1. **/api/auth/request-code**  
   User registration and authentication via phone number (simulation).

2. **/api/auth/verify-code**  
   Verification of the authorization code entered by the user.

3. **/api/users/activate-invite-code**  
   Activating an invite (referral) code.

4. **/api/users/profile**  
   Retrieving the user's profile information (including their referrals).

### API Documentation

1. **/api/docs/**  
   API documentation in Swagger UI format (available only in development mode).

2. **/api/redoc/**  
   API documentation in Redoc format (available only in development mode).

3. **/api/schema/**  
   OpenAPI schema for the API (available only in development mode).

### User Interface

1. **/profile/**  
   User profile page.

2. **/request_code/**  
   Page to request the authorization code (simulation).

3. **/verify_code/**  
   Page to verify the authorization code.

## How to Use

### Documentation in Development Mode

API documentation is available only in development mode. You can access it via the following URLs:

- **Swagger UI**: `http://127.0.0.1:8000/api/docs/`
- **Redoc**: `http://127.0.0.1:8000/api/redoc/`
- **OpenAPI Schema**: `http://127.0.0.1:8000/api/schema/`

These endpoints are only available if the project is running in development mode (DEBUG=True).

## Deployment on Heroku

The project is deployed on the Heroku platform and is available at the following address:  
[Heroku App](https://test-task-referral-system-92eb6c8cfef3.herokuapp.com/)


# RU

## Описание

Это проект реферальной системы, написанный на Django с использованием Django Rest Framework (DRF). Система позволяет
пользователям регистрироваться с помощью симуляции отправки кода (по факту проверка кода происходит через базу данных), а также
генерировать и активировать инвайт-коды.

Проект включает в себя:

- Авторизацию по номеру телефона (симуляция)
- Генерацию инвайт-кодов
- API для работы с функционалом
- Интерфейс на основе Django Templates
- Деплой на платформу Heroku (доступно по адресу https://test-task-referral-system-92eb6c8cfef3.herokuapp.com/)

## Установка

### Требования

- Python 3.10 или выше
- PostgreSQL
- Docker

### Установка зависимостей

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/YuryHaurylenka/test_task_referral.git
   cd test_task_referral
   ```

2. Создайте файл .env в корне проекта и добавьте следующие переменные:
   ```bash
   SECRET_KEY='your_secret_key'
   
   DEBUG=True
   ALLOWED_HOSTS='localhost, 127.0.0.1,'
   
   API_BASE_URL=http://127.0.0.1:8000/api
   
   # credentials 
   POSTGRES_DB=referral_system
   POSTGRES_USER=referral_user
   POSTGRES_PASSWORD=securepassword
   POSTGRES_HOST=db
   POSTGRES_PORT=5432
   ```

## Запуск проекта

1. Сборка и запуск контейнеров:
   ```bash
   docker-compose build
   docker-compose up
   ```

2. Примените миграции базы данных:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

3. После того как контейнеры запустятся, проект будет доступен по адресу http://127.0.0.1:8000


## Структура приложения

### API Endpoints

1. **/api/auth/request-code**  
   Регистрация и авторизация пользователей по номеру телефона (симуляция).

2. **/api/auth/verify-code**  
   Верификация кода авторизации, введенного пользователем.

3. **/api/users/activate-invite-code**  
   Активация инвайт-кода (реферального кода).

4. **/api/users/profile**  
   Получение информации о профиле пользователя (включая его рефереров).

### Документация API

1. **/api/docs/**  
   Документация API в формате Swagger UI (только в режиме разработки).

2. **/api/redoc/**  
   Документация API в формате Redoc (только в режиме разработки).

3. **/api/schema/**  
   Схема OpenAPI для API (только в режиме разработки).

### Интерфейс

1. **/profile/**  
   Страница профиля пользователя.

2. **/request_code/**  
   Страница запроса кода авторизации (симуляция).

3. **/verify_code/**  
   Страница для верификации кода авторизации.

## Как использовать

### Документация в режиме разработки

Документация API доступна только в режиме разработки. Вы можете получить доступ к ней по следующим адресам:

- **Swagger UI**: `http://127.0.0.1:8000/api/docs/`
- **Redoc**: `http://127.0.0.1:8000/api/redoc/`
- **OpenAPI Schema**: `http://127.0.0.1:8000/api/schema/`

Эти эндпоинты доступны только если проект работает в режиме разработки (DEBUG=True).

## Деплой на Heroku

Проект задеплоен на платформе Heroku и доступен по следующему адресу:  
[Heroku App](https://test-task-referral-system-92eb6c8cfef3.herokuapp.com/)
