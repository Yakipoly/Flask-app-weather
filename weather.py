# -*- coding: utf-8 -*-
import requests


def fetch_coordinates(city: str) -> dict:
    """
    Получить координаты (широту и долготу) данного города.
    Args:
        city (str): Название города
    Returns:
        dict: Словарь состоящий из latitude и longitude или поля error
    """

    try:
        response = requests.get(
            f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=ru&format=json"
        )
    except requests.exceptions.RequestException as e:
        return {"error": "Ошибка сети"}

    if response.status_code != 200:
        return {"error": "Город не найден"}

    data = response.json().get("results", [])

    if not data:
        return {"error": "Город не найден"}

    if "latitude" not in data[0] and "longitude" not in data[0]:
        return {"error": "Координаты не найдены"}

    return data[0]


def fetch_weather(city: str) -> dict:
    """
    Функция для получения температуры в указанном городе
    Args:
        city (str): Название города
    Returns:
        dict: Словарь состоящий из поля error или поля temperature в градусах Цельсия
    """

    coordinates = fetch_coordinates(city)
    if "error" in coordinates:
        return {"error": coordinates["error"]}

    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={coordinates['latitude']}&longitude={coordinates['longitude']}&current=temperature_2m"
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        return {"error": "Ошибка сети"}

    if response.status_code != 200:
        return {"error": "Погода не определена"}

    data = response.json()
    if "current" not in data or "temperature_2m" not in data["current"]:
        return {"error": "Неправильные координаты"}

    return {"temperature": data["current"]["temperature_2m"]}
