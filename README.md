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

1. **/api/auth/**  
   User registration and authentication via phone number (simulation)

2. **/api/users/**  
   User management (CRUD)

3. **/api/redoc/**  
   API documentation in Redoc format

4. **/api/docs/**  
   API documentation in Swagger UI format

### Interface

1. **/profile/**  
   User profile page

2. **/request_code/**  
   Page to request an authorization code (simulation)

3. **/verify_code/**  
   Page to verify the authorization code

## How to Use

1. **Enter Phone Number**  
   Go to the `/request_code/` page and enter your phone number. The system will simulate sending a code and store it in the database.

2. **Enter Code**  
   You will be redirected to the `/verify_code/` page. Enter the received code. If the code is correct, you will be redirected to the profile page.

3. **Profile**  
   On the `/profile/` page, you will be able to see information about your profile. There is also a button for logging out (logout).

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

1. **/api/auth/**  
   Регистрация и авторизация пользователей по номеру телефона (симуляция)

2. **/api/users/**  
   Работа с пользователями (CRUD)

3. **/api/redoc/**  
   Документация API в формате Redoc

4. **/api/docs/**  
   Документация API в формате Swagger UI

### Интерфейс

1. **/profile/**  
   Страница профиля пользователя

2. **/request_code/**  
   Страница запроса кода авторизации (симуляция)

3. **/verify_code/**  
   Страница для верификации кода авторизации

## Как пользоваться

1. **Ввод номера телефона**  
   Перейдите на страницу `/request_code/` и введите ваш номер телефона. Система сымитирует отправку кода и сохранит его в базе данных.

2. **Ввод кода**  
   Вас редиректнет на страницу `/verify_code/`, далее введите полученный код. Если код введен правильно, вы будете перенаправлены на страницу профиля.

3. **Профиль**  
   На странице `/profile/` вы сможете увидеть информацию о вашем профиле. Здесь же доступна кнопка для выхода (logout).

## Деплой на Heroku

Проект задеплоен на платформе Heroku и доступен по следующему адресу:  
[Heroku App](https://test-task-referral-system-92eb6c8cfef3.herokuapp.com/)
