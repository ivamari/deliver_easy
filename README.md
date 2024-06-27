# Сервис для доставки сети кафе

## Описание
Сервис доставки для сети кафе, который позволяет пользователям добавлять товары в корзину и совершать заказы. Система автоматически определяет ближайшее кафе для доставки на основе геолокации пользователя. Проект выполнен с использованием Django REST Framework (DRF) и GeoDjango для определения локации пользователя и ближайшего к нему кафе. Реализована кастомная система регистрации пользователей. В проекте используется PostgreSQL с расширением PostGIS для работы с геоданными.

Технологии
* • Python
* • Django REST Framework (DRF)
* • PostgreSQL с расширением PostGIS

## Основной функционал
### Сотрудники, Клиенты
**Возможности:**
1. Регистрация сотрудника (доступна только администратору), регистрация клиента
2. Просмотр и изменение профиля сотрудника (доступна только администратору), просмотр и изменение профиля клиента

### Кафе
**Возможности для администраторов:**
1. Просмотр кафе
2. Изменение кафе
3. Просмотр списка кафе
4. Частичное изменение кафе

### Кафе: Сотрудники
**Возможности:**
1. Просмотр списка сотрудников, деталка сотрудника кафе
2. Удаление сотрудника из кафе
3. Обновление должности сотрудника кафе

### Кафе: Должности
**Возможности:**
1. Создание должности
2. Просмотр списка должностей
3. Просмотр должности
4. Изменение должности

### Отделы
**Возможности:**
1. Просмотр списка всех отделов

### Корзины
**Возможности:**
1. Получение корзины пользователя по id пользователя (для администраторов)
2. Получение своей корзины
3. Добавление товара в корзину
4. Удаление товара из корзины
5. Изменение количества товара в корзине

### Заказы
**Возможности:**
1. Создание заказа
2. Просмотр заказов пользователя по id пользователя (для администраторов)
3. Просмотр заказа
4. Просмотр списка своих заказов

### Товары: Категории
**Возможности:**
1. Создание категории
2. Просмотр списка категорий
3. Просмотр категории
4. Частичное изменение категории

### Товары
**Возможности:**
1. Список товаров
2. Добавление товара
3. Получение товара
4. Изменение товара



