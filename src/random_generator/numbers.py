"""Модуль генерації випадкових чисел у заданому діапазоні."""

import random


def random_integer(min_val: int, max_val: int) -> int:
    """Повертає випадкове ціле число в діапазоні [min_val, max_val] включно.

    Args:
        min_val: Нижня межа діапазону.
        max_val: Верхня межа діапазону.

    Returns:
        Випадкове ціле число.

    Raises:
        TypeError: Якщо межі не є цілими числами (або є bool).
        ValueError: Якщо min_val більше за max_val.
    """
    if isinstance(min_val, bool) or isinstance(max_val, bool):
        raise TypeError("Межі діапазону повинні бути цілими числами, а не bool.")
    if not isinstance(min_val, int) or not isinstance(max_val, int):
        raise TypeError("Межі діапазону повинні мати тип int.")
    if min_val > max_val:
        raise ValueError("min_val не може бути більшим за max_val.")

    return random.randint(min_val, max_val)


def random_float(min_val: float = 0.0, max_val: float = 1.0, decimals: int | None = None) -> float:
    """Повертає випадкове число з плаваючою комою в діапазоні [min_val, max_val].

    Args:
        min_val: Нижня межа діапазону (за замовчуванням 0.0).
        max_val: Верхня межа діапазону (за замовчуванням 1.0).
        decimals: Кількість знаків після коми для заокруглення (за замовчуванням None).

    Returns:
        Випадкове число з плаваючою комою.

    Raises:
        TypeError: Якщо межі або decimals мають некоректний тип.
        ValueError: Якщо min_val більше за max_val або decimals < 0.
    """
    if isinstance(min_val, bool) or isinstance(max_val, bool):
        raise TypeError("Межі діапазону не повинні бути типу bool.")
    if not isinstance(min_val, (int, float)) or not isinstance(max_val, (int, float)):
        raise TypeError("Межі діапазону повинні бути числами (int або float).")
    if min_val > max_val:
        raise ValueError("min_val не може бути більшим за max_val.")

    value = random.uniform(float(min_val), float(max_val))

    if decimals is not None:
        if isinstance(decimals, bool) or not isinstance(decimals, int):
            raise TypeError("Параметр decimals повинен бути цілим числом або None.")
        if decimals < 0:
            raise ValueError("Параметр decimals не може бути від'ємним.")
        value = round(value, decimals)

    return value