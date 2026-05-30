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
├── models/ # SQLAlchemy 2.0 модели (User, Restaurant, MenuItem, Order, OrderItem)
│ ├── init.py
│ ├── user.py 
│ ├── restaurant.py 
│ ├── menu_item.py 
│ ├──database.py
│ └── order.py 
└── main.py 
└── factories.py 
└──seed.py 

alembic/ # Миграции базы данных (Alembic)
├── versions/ # Файлы миграций
├── env.py # Конфигурация окружения Alembic
└── alembic.ini # Настройки подключения к БД

README.md 
