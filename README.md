

## Тестовое задание

- Создать веб приложение используя Flask
- При запуске приложения создается простая база данных SQLite, для управления списком пользователей(`users`) с полями(`id`, `username`, `balance`) с 5 пользователями и балансом от 5000 до 15000
- Напишите Python-класс `User`, который представляет пользователя и взаимодействует с базой данных для добавления, обновления и удаления пользователей и обновления их балансов
- Используя библиотеку `requests`, напишите функцию `fetch_weather(city)`, которая принимает на вход название города и возвращает текущую температуру в этом городе. Используйте любое открытое API для получения данных о погоде. Важно, вы можете использовать погрешность, температура меняется не чаще 10 минут
- Написать route для обновления баланса пользователя, как в большую, так и в меньшую сторону на сумму равную температуре воздуха в выбранном городе, принимающего параметры userId, city.
- Важным условием является то, что баланс пользователя не может быть отрицательным.
- Изменение баланса должно производиться в реальном времени, без использования очередей и отложенных задач.


## Описание API

1. **GET /users**
    - **Описание:** Эта конечная точка извлекает всех пользователей.
    - **Метод:** GET
    - **Параметры:** Нет
    - **Возвращает:** JSON-ответ, содержащий всех пользователей.

2. **GET /users/<city>/<user_id>**
    - **Описание:** Эта конечная точка извлекает погоду для определенного города и обновляет баланс пользователя на основе температуры.
    - **Метод:** GET
    - **Параметры:**
        - city (строка): Название города, для которого запрашивается погода.
        - user_id (целое число): Уникальный идентификатор пользователя.
    - **Возвращает:**
        - В случае успешного выполнения возвращает JSON-ответ, содержащий название города, идентификатор пользователя, температуру города и результат обновления баланса пользователя.
        - Если возникли ошибки (например, недопустимый идентификатор пользователя или ошибка при получении данных о погоде), в ответе возвращаются соответствующие сообщения об ошибке.


> В качестве форматировщика кода Python использовался black