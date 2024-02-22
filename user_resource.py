# -*- coding: utf-8 -*-
from user_model import User
from db import db
from random import randint


def create_users_if_not_exists(amount: int) -> None:
    """
    Функция для создания пользователей, если они не существуют в базе данных.

    Args:
        amount (int): Количество пользователей, которое нужно создать.

    Returns:
        None
    """
    users = User.query.all()
    if users:
        return
    for user_id in range(1, amount + 1):
        new_user = User(username=f"user{user_id}", balance=randint(5000, 15000))
        db.session.add(new_user)

    db.session.commit()


def get_all_users() -> list:
    """
    Функция для получения списка всех пользователей.

    Returns:
        list: Список словарей с информацией о каждом пользователе (id, username, balance).
    """
    users = User.query.all()
    users_list = []
    for user in users:
        user_data = {"id": user.id, "username": user.username, "balance": user.balance}
        users_list.append(user_data)
    return users_list


def update_balance_by_id(user_id: int, amount: int):
    """
    Функция для обновления баланса пользователя по его идентификатору.

    Args:
        user_id (int): Идентификатор пользователя.
        amount (int): Сумма, на которую нужно обновить баланс.

    Returns:
        dict: Результат обновления баланса пользователя или сообщение об ошибке.
    """
    user = User.query.get(user_id)
    if not user:
        return {"error": "Пользователь с указанным id не найден"}

    new_balance = user.balance + amount
    if new_balance < 0:
        return {"error": "Новый баланс не может быть отрицательным."}

    user.balance = new_balance
    db.session.commit()

    return {
        "result": f"Баланс пользователя с id={user_id} успешно обновлен на {amount}. Новый баланс: {user.balance}"
    }
