# Сервис для доставки сети кафе (deliver_easy)

## Описание
Сервис доставки для сети кафе, позволяющий пользователям добавлять товары в корзину и совершать заказы. Система автоматически определяет ближайшее кафе для доставки на основе геолокации пользователя. Проект выполнен с использованием DRF и GeoDjango для определения локации пользователя и ближайшего к нему кафе. Реализована кастомная система регистрации пользователей. Использована PostgreSQL с расширением PostGIS для работы с геоданными. 

Технологии: Python, DRF, PostgreSQL с расширением PostGIS

## Основной функционал
### Сотрудники
**Возможности:**
1. Регистрация сотрудника (доступна только администратору)
2. Просмотр и изменение профиля сотрудника (доступна только администратору)

### Клиенты
**Возможности:**
1. Регистрация клиента
2. Просмотр и изменение профиля

### Кафе
**Возможности для администраторов:**
1. Просмотр кафе
2. Изменение кафе
3. Просмотр списка кафе
4. Частичное изменение кафе

### Кафе: Сотрудники
**Возможности:**
1. Просмотр списка сотрудников кафе
2. Удаление сотрудника из кафе
3. Обновление должности сотрудника кафе

### Кафе: Должности
**Возможности:**
1. Создание должности
2. Список должностей
3. Получение должности
4. Изменение должности

### Отделы
**Возможности:**
1. Просмотр списка всех отделов

### Товары: Категории
**Возможности:**
1. Создание котегории
2. Просмтр списка категорий
3. Просмотр категории
4. Частичное изменение категории

