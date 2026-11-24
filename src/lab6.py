"""Головний модуль лабораторної роботи № 6 (Варіант 9: random_generator)."""

import math
from rich.console import Console
from rich.table import Table

from .random_generator import random_choice, random_float, random_integer


def run_demo() -> None:
    """Демонструє роботу пакета random_generator, модуля math та пакета rich."""
    console = Console()

    # Використання власного пакета random_generator
    rand_int = random_integer(1, 100)
    rand_flt = random_float(1.0, 25.0, decimals=3)
    variants = ["Python", "C#", "C++", "Git", "UnitTest"]
    picked_item = random_choice(variants)

    # Використання модуля стандартної бібліотеки math
    sqrt_of_float = math.sqrt(rand_flt)
    ceil_of_float = math.ceil(rand_flt)

    # Використання стороннього пакета rich
    table = Table(title="Результати роботи пакета random_generator (Варіант 9)")
    table.add_column("Функція / Джерело", style="cyan")
    table.add_column("Отримане значення", style="green")

    table.add_row("random_integer(1, 100)", str(rand_int))
    table.add_row("random_float(1.0, 25.0, decimals=3)", str(rand_flt))
    table.add_row("random_choice(variants)", str(picked_item))
    table.add_row("math.sqrt(rand_flt)", f"{sqrt_of_float:.4f}")
    table.add_row("math.ceil(rand_flt)", str(ceil_of_float))

    console.print(table)


if __name__ == "__main__":
    run_demo()