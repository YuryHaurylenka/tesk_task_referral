# Referral System

# EN

## Description

This is a referral system project built with Django and Django Rest Framework (DRF). The system allows users to register via a simulated code sending process (in reality, the code is checked through the database), as well as generate and activate invite codes.

---

## Features

### 1. Phone Number Authorization
- First request prompts the user to input their phone number.
- Simulates sending a 4-digit authorization code.
- Second request prompts the user to input the received code.
- If the user is logging in for the first time, their data is saved in the database.

### 2. Random Invite Code Generation
- On first login, a random 6-character invite code (letters and numbers) is generated for the user.

### 3. User Profile Management
- Users can view their profile, which includes:
  - Their invite code.
  - An option to activate another user's invite code.
- **Invite Code Activation**:
  - Users can activate only one and once invite code.
  - If an invite code is already activated, it is displayed in the profile.
  - Validation ensures the invite code exists before activation.

### 4. Referral Tracking
- The profile API includes a list of phone numbers of users who activated the current user's invite code.

### 5. API Documentation
- Full API for all features (authorization, invite code activation, profile management).
- Includes endpoints for:
  - Phone number login.
  - Code verification.
  - Profile retrieval and editing.
- Documented API.

### 6. Django templates
- A simple user interface for the application.

### 7. Free Hosting
- Deployed on **Heroku**.

### 8. Containerization
- If you don't use in prod, containerized by **Docker**.

---

## Deployment on Heroku

The project is deployed on the Heroku platform and is available at the following address:  
[Heroku App](https://test-task-r# Referral System

# EN

## Description

This is a referral system project built with Django and Django Rest Framework (DRF). The system allows users to register via a simulated code sending process (in reality, the code is checked through the database), as well as generate and activate invite codes.

---

## Features

### 1. Phone Number Authorization
- First request prompts the user to input their phone number.
- Simulates sending a 4-digit authorization code.
- Second request prompts the user to input the received code.
- If the user is logging in for the first time, their data is saved in the database.

### 2. Random Invite Code Generation
- On first login, a random 6-character invite code (letters and numbers) is generated for the user.

### 3. User Profile Management
- Users can view their profile, which includes:
  - Their invite code.
  - An option to activate another user's invite code.
- **Invite Code Activation**:
  - Users can activate only one and once invite code.
  - If an invite code is already activated, it is displayed in the profile.
  - Validation ensures the invite code exists before activation.

### 4. Referral Tracking
- The profile API includes a list of phone numbers of users who activated the current user's invite code.

### 5. API Documentation
- Full API for all features (authorization, invite code activation, profile management).
- Includes endpoints for:
  - Phone number login.
  - Code verification.
  - Profile retrieval and editing.
- Documented API.

### 6. Django templates
- A simple user interface for the application.

### 7. Free Hosting
- Deployed on **Heroku**.

### 8. Containerization
- If you don't use in prod, containerized by **Docker**.

---

## Deployment on Heroku

The project is deployed on the Heroku platform and is available at the following address:  
[Heroku App](https://test-task-referral-system-92eb6c8cfef3.herokuapp.com)

## Installation

### Requirements

- Python 3.10 or higher
- PostgreSQL
- Docker

---

## Installing Dependencies

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
---

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

---

### API Documentation

1. **/api/docs/**  
   API documentation in Swagger UI format (available only in development mode).

2. **/api/redoc/**  
   API documentation in Redoc format (available only in development mode).

3. **/api/schema/**  
   OpenAPI schema for the API (available only in development mode).

---

### User Interface

1. **/profile/**  
   User profile page.

2. **/request_code/**  
   Page to request the authorization code (simulation).

3. **/verify_code/**  
   Page to verify the authorization code.

---

## How to Use

1. **Enter Phone Number**  
   Go to the `/request_code/` page and enter your phone number. The system will simulate sending a code and store it in the database.

2. **Enter Code**  
   You will be redirected to the `/verify_code/` page. Enter the received code from db. If the code is correct, you will be redirected to the profile page.

3. **Profile**  
   On the `/profile/` page, you will be able to see information about your profile. There is also a button for logging out (logout).

### Documentation in Development Mode

API documentation is available only in development mode. You can access it via the following URLs:

- **Swagger UI**: `http://127.0.0.1:8000/api/docs/`
- **Redoc**: `http://127.0.0.1:8000/api/redoc/`
- **OpenAPI Schema**: `http://127.0.0.1:8000/api/schema/`

These endpoints are only available if the project is running in development mode (DEBUG=True).

---

# RU

## Описание

Это проект реферальной системы, написанный на Django с использованием Django Rest Framework (DRF). Система позволяет
пользователям регистрироваться с помощью симуляции отправки кода (по факту проверка кода происходит через базу данных), а также
генерировать и активировать инвайт-коды.

---

## Функционал

### 1. Авторизация по номеру телефона
- Первый запрос предлагает пользователю ввести свой номер телефона.
- Симуляция отправки 4-значного кода авторизации.
- Второй запрос предлагает пользователю ввести полученный код.
- Если пользователь входит в систему впервые, его данные сохраняются в базе данных.

### 2. Генерация случайного инвайт-кода
- При первом входе генерируется случайный 6-значный инвайт-код (буквы и цифры) для пользователя.

### 3. Управление профилем пользователя
- Пользователи могут просматривать свой профиль, который включает:
  - Инвайт-код пользователя.
  - Опцию активации инвайт-кода другого пользователя.
- **Активация инвайт-кода**:
  - Пользователи могут активировать только один инвайт-код, и это можно сделать только один раз.
  - Если инвайт-код уже активирован, он отображается в профиле.
  - Валидируется, что инвайт-код существует перед активацией.

### 4. Отслеживание рефералов
- В API профиля содержится список номеров телефонов пользователей, которые активировали инвайт-код текущего пользователя.

### 5. Документация API
- Полная документация API для всех эндпоинтов (авторизация, активация инвайт-кодов, управление профилем).

### 6. Использование шаблонов Django
- Простой пользовательский интерфейс для приложения.

### 7. Бесплатный хостинг
- Деплой на **Heroku**.

### 8. Контейнеризация
- Если не использовать в проде, контейнезирация с помощью **Docker**.

---

## Deployment on Heroku

The project is deployed on the Heroku platform and is available at the following address:  
[Heroku App](https://test-task-referral-system-92eb6c8cfef3.herokuapp.com)

---

## Установка

### Требования

- Python 3.10 или выше
- PostgreSQL
- Docker

---

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
---

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

---

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

---

### Документация API

1. **/api/docs/**  
   Документация API в формате Swagger UI (только в режиме разработки).

2. **/api/redoc/**  
   Документация API в формате Redoc (только в режиме разработки).

3. **/api/schema/**  
   Схема OpenAPI для API (только в режиме разработки).

---

### Интерфейс

1. **/profile/**  
   Страница профиля пользователя.

2. **/request_code/**  
   Страница запроса кода авторизации (симуляция).

3. **/verify_code/**  
   Страница для верификации кода авторизации.

---

## Как использовать

1. **Введите номер телефона**  
   Перейдите на страницу `/request_code/` и введите ваш номер телефона. Система сымитирует отправку кода и сохранит его в базе данных.

2. **Введите код для авторизации**  
   Вас перенаправит на страницу `/verify_code/`. Введите полученный код из БД. Если всё правильно, вы будете перенаправлены на страницу профиля.

3. **Profile**
   На странице `/profile/` вы сможете увидеть информацию о вашем профиле. Также будет доступна кнопка для выхода (logout).

---

### Документация в режиме разработки

Документация API доступна только в режиме разработки. Вы можете получить доступ к ней по следующим адресам:

- **Swagger UI**: `http://127.0.0.1:8000/api/docs/`
- **Redoc**: `http://127.0.0.1:8000/api/redoc/`
- **OpenAPI Schema**: `http://127.0.0.1:8000/api/schema/`

Эти эндпоинты доступны только если проект работает в режиме разработки (DEBUG=True).
eferral-system-92eb6c8cfef3.herokuapp.com/)

## Installation

### Requirements

- Python 3.10 or higher
- PostgreSQL
- Docker

---

## Installing Dependencies

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
---

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

---

### API Documentation

1. **/api/docs/**  
   API documentation in Swagger UI format (available only in development mode).

2. **/api/redoc/**  
   API documentation in Redoc format (available only in development mode).

3. **/api/schema/**  
   OpenAPI schema for the API (available only in development mode).

---

### User Interface

1. **/profile/**  
   User profile page.

2. **/request_code/**  
   Page to request the authorization code (simulation).

3. **/verify_code/**  
   Page to verify the authorization code.

---

## How to Use

1. **Enter Phone Number**  
   Go to the `/request_code/` page and enter your phone number. The system will simulate sending a code and store it in the database.

2. **Enter Code**  
   You will be redirected to the `/verify_code/` page. Enter the received code from db. If the code is correct, you will be redirected to the profile page.

3. **Profile**  
   On the `/profile/` page, you will be able to see information about your profile. There is also a button for logging out (logout).

### Documentation in Development Mode

API documentation is available only in development mode. You can access it via the following URLs:

- **Swagger UI**: `http://127.0.0.1:8000/api/docs/`
- **Redoc**: `http://127.0.0.1:8000/api/redoc/`
- **OpenAPI Schema**: `http://127.0.0.1:8000/api/schema/`

These endpoints are only available if the project is running in development mode (DEBUG=True).

---

# RU

## Описание

Это проект реферальной системы, написанный на Django с использованием Django Rest Framework (DRF). Система позволяет
пользователям регистрироваться с помощью симуляции отправки кода (по факту проверка кода происходит через базу данных), а также
генерировать и активировать инвайт-коды.

---

## Функционал

### 1. Авторизация по номеру телефона
- Первый запрос предлагает пользователю ввести свой номер телефона.
- Симуляция отправки 4-значного кода авторизации.
- Второй запрос предлагает пользователю ввести полученный код.
- Если пользователь входит в систему впервые, его данные сохраняются в базе данных.

### 2. Генерация случайного инвайт-кода
- При первом входе генерируется случайный 6-значный инвайт-код (буквы и цифры) для пользователя.

### 3. Управление профилем пользователя
- Пользователи могут просматривать свой профиль, который включает:
  - Инвайт-код пользователя.
  - Опцию активации инвайт-кода другого пользователя.
- **Активация инвайт-кода**:
  - Пользователи могут активировать только один инвайт-код, и это можно сделать только один раз.
  - Если инвайт-код уже активирован, он отображается в профиле.
  - Валидируется, что инвайт-код существует перед активацией.

### 4. Отслеживание рефералов
- В API профиля содержится список номеров телефонов пользователей, которые активировали инвайт-код текущего пользователя.
- 
### 5. Документация API
- Полная документация API для всех эндпоинтов (авторизация, активация инвайт-кодов, управление профилем).

### 6. Использование шаблонов Django
- Простой пользовательский интерфейс для приложения.

### 7. Бесплатный хостинг
- Деплой на **Heroku**.

### 8. Контейнеризация
- Если не использовать в проде, контейнезирация с помощью **Docker**.

---

## Deployment on Heroku

The project is deployed on the Heroku platform and is available at the following address:  
[Heroku App](https://test-task-referral-system-92eb6c8cfef3.herokuapp.com/)

---

## Установка

### Требования

- Python 3.10 или выше
- PostgreSQL
- Docker

---

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
---

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

---

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

---

### Документация API

1. **/api/docs/**  
   Документация API в формате Swagger UI (только в режиме разработки).

2. **/api/redoc/**  
   Документация API в формате Redoc (только в режиме разработки).

3. **/api/schema/**  
   Схема OpenAPI для API (только в режиме разработки).

---

### Интерфейс

1. **/profile/**  
   Страница профиля пользователя.

2. **/request_code/**  
   Страница запроса кода авторизации (симуляция).

3. **/verify_code/**  
   Страница для верификации кода авторизации.

---

## Как использовать

1. **Введите номер телефона**  
   Перейдите на страницу `/request_code/` и введите ваш номер телефона. Система сымитирует отправку кода и сохранит его в базе данных.

2. **Введите код для авторизации**  
   Вас перенаправит на страницу `/verify_code/`. Введите полученный код из БД. Если всё правильно, вы будете перенаправлены на страницу профиля.

3. **Profile**
   На странице `/profile/` вы сможете увидеть информацию о вашем профиле. Также будет доступна кнопка для выхода (logout).

---

### Документация в режиме разработки

Документация API доступна только в режиме разработки. Вы можете получить доступ к ней по следующим адресам:

- **Swagger UI**: `http://127.0.0.1:8000/api/docs/`
- **Redoc**: `http://127.0.0.1:8000/api/redoc/`
- **OpenAPI Schema**: `http://127.0.0.1:8000/api/schema/`

Эти эндпоинты доступны только если проект работает в режиме разработки (DEBUG=True).
