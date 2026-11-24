"""Модуль випадкового вибору елементів із послідовностей."""

import random
from typing import Sequence, TypeVar

T = TypeVar("T")


def random_choice(items: Sequence[T]) -> T:
    """Повертає випадковий елемент із непорожнього списку чи іншої послідовності.

    Args:
        items: Послідовність елементів (наприклад, список або кортеж).

    Returns:
        Випадково обраний елемент.

    Raises:
        ValueError: Якщо передано порожню послідовність.
    """
    if not items:
        raise ValueError("Неможливо вибрати елемент із порожньої послідовності.")

    return random.choice(items)