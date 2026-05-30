# # 🚚 Сервис доставки еды (Food Delivery MVP)
> Информационная система для автоматизации заказа, приготовления и доставки еды. Охватывает полный цикл взаимодействия ролей: **Клиент**, **Ресторан**, **Курьер**, **Администратор**.

## 🎯 Цель проекта
Разработка MVP-приложения с прозрачным бизнес-процессом, надёжным слоем данных и командной разработкой по методологии **Scrumban**.

## 🛠 Технологический стек
| Компонент | Технология | Обоснование |
|---|---|---|
| **Backend** | Python 3.11+ + FastAPI | Асинхронность, автогенерация OpenAPI/Swagger |
| **ORM** | SQLAlchemy 2.0 | Современный декларативный синтаксис (`Mapped`, `mapped_column`), строгая типизация |
| **БД** | PostgreSQL (prod) / SQLite (dev) | MVCC, транзакции, JSONB. SQLite оставлен для локальной разработки |
| **Миграции** | Alembic | Версионирование схемы БД, `upgrade`/`downgrade` |
| **Frontend** | React / Vue.js (SPA) | Компонентный подход, динамический UI |
| **Тестовые данные** | `factory_boy` + `Faker` | Реалистичные фикстуры, автоматическое создание связанных сущностей |
| **DevOps & CI/CD** | Docker, GitHub Actions, Nginx | Воспроизводимость окружения, автоматизация сборки |
| **Управление проектом** | GitHub Projects (Kanban), Git Flow | Визуализация потока, WIP-лимиты, Feature Branch + Pull Request |

## 📂 Структура репозитория
```text
app/
├── api/ # API эндпоинты (роутеры FastAPI)
├── core/ # Конфигурация, зависимости (config, deps)
├── models/ # SQLAlchemy 2.0 модели (User, Restaurant, MenuItem, Order, OrderItem)
│ ├── init.py
│ ├── user.py # Модель пользователя (клиент, курьер, админ)
│ ├── restaurant.py # Модель ресторана
│ ├── menu_item.py # Модель блюда меню
│ └── order.py # Модели заказа и позиций заказа
├── schemas/ # Pydantic схемы для валидации запросов/ответов
├── database.py # Подключение к БД, Base, SessionLocal
└── main.py # Точка входа FastAPI приложения

alembic/ # Миграции базы данных (Alembic)
├── versions/ # Файлы миграций
├── env.py # Конфигурация окружения Alembic
└── alembic.ini # Настройки подключения к БД

factories/ # Фабрики для генерации тестовых/seed данных
├── init.py
└── factories.py # UserFactory, RestaurantFactory, MenuItemFactory, OrderFactory

tests/ # Юнит- и интеграционные тесты

docs/ # Документация проекта
├── BPMN/ # Диаграммы бизнес-процессов
├── ERD/ # ER-диаграммы базы данных
└── Use_Case/ # Use Case диаграммы

seed.py # Скрипт для наполнения БД тестовыми данными
docker-compose.yml # Docker Compose конфигурация
requirements.txt # Зависимости Python
README.md # Документация проекта
