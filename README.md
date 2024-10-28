## Описание
# Сервис для доставки сети кафе
Сервис доставки для сети кафе, который позволяет пользователям добавлять товары в корзину и совершать заказы. Система автоматически определяет ближайшее кафе для доставки на основе геолокации пользователя. Проект выполнен с использованием Django REST Framework (DRF) и GeoDjango для определения локации пользователя и ближайшего к нему кафе. Реализована кастомная система регистрации пользователей. В проекте используется PostgreSQL с расширением PostGIS для работы с геоданными.

Технологии
* Python
* Django REST Framework (DRF)
* PostgreSQL с расширением PostGIS
  
## Основной функционал
### Пользователи
**Регистрация**
* Регистрация сотрудника (доступна только администратору)
* Регистрация клиента
**Профиль**
* Просмотр и изменение профиля сотрудника (доступно только администратору)
* Просмотр и изменение профиля клиента
  
### Кафе
**Управление кафе (для администраторов)**
* Просмотр кафе
* Изменение кафе
* Просмотр списка кафе
* Частичное изменение кафе
  
### Сотрудники кафе
**Управление сотрудниками**
* Просмотр списка сотрудников
* Просмотр информации о сотруднике кафе
* Удаление сотрудника из кафе
* Обновление должности сотрудника кафе
  
### Должности
**Управление должностями**
* Создание должности
* Просмотр списка должностей
* Просмотр информации о должности
* Изменение данных должности
  
### Отделы
**Управление отделами**
* Просмотр списка всех отделов
**Управление отделами кафе**
* Просмотр списка всех кафе с отделами
* Получение кафе с отделами
* Добавление отдела в кафе
  
### Корзины
**Управление корзиной**
* Получение корзины пользователя по ID (для администраторов)
* Получение своей корзины
* Добавление товара в корзину
* Удаление товара из корзины
* Изменение количества товара в корзине
  
### Заказы
**Управление заказами**
* Создание заказа
* Просмотр заказов пользователя по ID (для администраторов)
* Просмотр заказа
* Просмотр списка своих заказов
  
### Товары
**Категории товаров**
* Создание категории
* Просмотр списка категорий
* Просмотр информации о категории
* Частичное изменение данных категории

**Управление товарами**
* Просмотр списка товаров
* Добавление товара
* Просмотр информации о товаре
* Изменение данных товара

## Как запустить проект:
### Клонировать репозиторий и перейти в него в командной строке:
`https://github.com/ivamari/deliver_easy.git`
`cd deliver_easy`
### Cоздать и активировать виртуальное окружение:
`python3 -m venv env`
`source venv/bin/activate`
### Установить зависимости из файла requirements.txt:
`python3 -m pip install --upgrade pip`
`pip install -r requirements.txt`
### Выполнить миграции:
`python3 manage.py migrate`
### Запустить проект:
`python3 manage.py runserver`

## Примеры запросов к API
Примеры запросов и JSON ответы можно посмотреть в документации после запуска проекта по адресу: http://127.0.0.1:8000/api/
