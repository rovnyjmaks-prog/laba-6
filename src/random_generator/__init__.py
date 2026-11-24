"""Пакет random_generator для генерації випадкових чисел та вибору елементів."""

from .choices import random_choice
from .numbers import random_float, random_integer

__all__ = [
    "random_integer",
    "random_float",
    "random_choice",
]