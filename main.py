# -*- coding: utf-8 -*-
from flask import Flask, render_template
from user_resource import (
    create_users_if_not_exists,
    get_all_users,
    update_balance_by_id,
)
from weather import fetch_weather

# Создание Flask-приложения
app = Flask(__name__)
# Настройка пути к базе данных
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
# Настройка кодировки JSON для обработки символов, отличных от ASCII
app.config["JSON_AS_ASCII"] = False


# Создание таблицы в базе данных до первого запроса
@app.before_first_request
def create_tables():
    from db import db

    db.init_app(app)
    db.create_all()
    create_users_if_not_exists(5)


@app.route("/")
def home():
    """
    Эндпоинт для обработки запроса к главной странице.

    Returns:
        str: Шаблон "index.html".
    """
    return render_template("index.html")


@app.route("/users", methods=["GET"])
def get_users():
    """
    Эндпоинт для получения списка всех пользователей.

    Returns:
        list: Список всех пользователей из базы данных.
    """
    return get_all_users()


@app.route("/users/<city>/<user_id>", methods=["GET"])
def update_balance_user_by_city_weather(city: str, user_id: int):
    """
    Эндпоинт для обновления баланса пользователя в зависимости от погоды в указанном городе.

    Args:
        city (str): Название города.
        user_id (int): Идентификатор пользователя.

    Returns:
        dict: Информация о погоде в указанном городе и результат обновления баланса пользователя.
    """
    city = str(city)

    try:
        user_id = int(user_id)
    except ValueError:
        return {"status": "error", "msg": "user_id не является целым числом."}

    temperature = fetch_weather(city)
    if "error" in temperature:
        return {"error": temperature["error"]}

    result = update_balance_by_id(user_id, temperature["temperature"])
    if "error" in result:
        return {"error": result["error"]}

    return {
        "city": city,
        "user_id": user_id,
        "temperature": temperature["temperature"],
        "result": result["result"],
    }


if __name__ == "__main__":
    app.run(debug=False)
