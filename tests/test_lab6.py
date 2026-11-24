"""Юніт-тести для пакета random_generator та модуля src.lab6."""

import unittest
from unittest.mock import patch

from src.lab6 import run_demo
from src.random_generator import random_choice, random_float, random_integer


class TestRandomGenerator(unittest.TestCase):
    """Тести функцій пакету random_generator."""

    def test_random_integer_within_bounds(self) -> None:
        """Перевіряє, що випадкове ціле число потрапляє у вказаний діапазон."""
        for _ in range(50):
            val = random_integer(10, 20)
            self.assertIsInstance(val, int)
            self.assertGreaterEqual(val, 10)
            self.assertLessEqual(val, 20)

    def test_random_integer_invalid_bounds(self) -> None:
        """Перевіряє винятки при некоректних межах для random_integer."""
        with self.assertRaises(ValueError):
            random_integer(50, 10)
        with self.assertRaises(TypeError):
            random_integer(1.5, 10)  # type: ignore[arg-type]
        with self.assertRaises(TypeError):
            random_integer(True, 10)  # type: ignore[arg-type]

    def test_random_float_within_bounds_and_rounding(self) -> None:
        """Перевіряє діапазон та заокруглення для random_float."""
        for _ in range(50):
            val = random_float(0.0, 10.0, decimals=2)
            self.assertIsInstance(val, float)
            self.assertGreaterEqual(val, 0.0)
            self.assertLessEqual(val, 10.0)

        with patch("src.random_generator.numbers.random.uniform", return_value=3.14159):
            self.assertEqual(random_float(0.0, 10.0, decimals=2), 3.14)

    def test_random_float_invalid_args(self) -> None:
        """Перевіряє винятки при некоректних аргументах random_float."""
        with self.assertRaises(ValueError):
            random_float(10.0, 2.0)
        with self.assertRaises(ValueError):
            random_float(0.0, 1.0, decimals=-1)

    def test_random_choice_valid_and_empty(self) -> None:
        """Перевіряє вибір елемента зі списку та помилку на порожньому списку."""
        items = ["a", "b", "c"]
        chosen = random_choice(items)
        self.assertIn(chosen, items)

        with self.assertRaises(ValueError):
            random_choice([])

    @patch("src.lab6.Console.print")
    def test_run_demo_executes(self, mock_print: unittest.mock.MagicMock) -> None:
        """Перевіряє, що демонстраційна функція в src/lab6.py виконується без помилок."""
        run_demo()
        mock_print.assert_called_once()


if __name__ == "__main__":
    unittest.main()