# -*- coding: utf-8 -*-
from db import db


# Создала Python-класс `User`...
class User(db.Model):
    """
    Класс, представляющий модель пользователя в базе данных.

    Attributes:
        id (int): Поле для хранения идентификатора пользователя (primary key).
        username (str): Поле для хранения имени пользователя (не может быть пустым).
        balance (float): Поле для хранения баланса пользователя (по умолчанию 0.0).
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    balance = db.Column(db.Float, default=0.0)

    def __repr__(self):
        """
        Метод для представления объекта пользователя в виде строки.

        Returns:
            str: Строковое представление объекта пользователя.
        """
        return f"<User {self.username}>"

    def add_user(self, username, balance=0.0):
        """
        Метод для добавления нового пользователя в базу данных.

        Args:
            username (str): Имя нового пользователя.
            balance (float): Баланс нового пользователя (по умолчанию 0.0).
        """
        new_user = User(username=username, balance=balance)
        db.session.add(new_user)
        db.session.commit()

    def update_balance(self, username, new_balance):
        """
        Метод для обновления баланса пользователя по его имени.

        Args:
            username (str): Имя пользователя, чей баланс нужно обновить.
            new_balance (float): Новое значение баланса пользователя.
        """
        user = User.query.filter_by(username=username).first()
        if user:
            user.balance = new_balance
            db.session.commit()

    def delete_user(self, username):
        """
        Метод для удаления пользователя из базы данных по его имени.

        Args:
            username (str): Имя пользователя, которого нужно удалить.
        """
        user = User.query.filter_by(username=username).first()
        if user:
            db.session.delete(user)
            db.session.commit()
