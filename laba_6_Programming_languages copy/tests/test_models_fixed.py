import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'fin_app'))

import unittest
from models import Expense, Category  # теперь без fin_app.

class TestCategory(unittest.TestCase):
    def test_category_creation(self):
        """Создание категории"""
        category = Category("Еда")
        self.assertEqual(category.name, "Еда")

class TestExpense(unittest.TestCase):
    def test_expense_has_attributes(self):
        """Проверка наличия атрибутов"""
        expense = Expense(1000.5, "Еда", "Обед")
        self.assertTrue(hasattr(expense, 'amount'))
        self.assertTrue(hasattr(expense, 'category'))
        self.assertTrue(hasattr(expense, 'description'))

    def test_expense_str_method(self):
        """Проверка строкового представления"""
        expense = Expense(1000.5, "Еда", "Обед")
        expected = f"Расход: {expense.amount} руб. на {expense.category} ({expense.description})"
        self.assertEqual(str(expense), expected)

    def test_expense_creation_order(self):
        """Тест правильного порядка параметров в Expense"""
        # В models.py НАМЕРЕННО ошибка: amount и category перепутаны
        expense = Expense(1000.5, "Еда", "Обед")

        # Если порядок правильный — amount = 1000.5, category = "Еда"
        # Но если ошибка — наоборот
        if isinstance(expense.amount, str) and isinstance(expense.category, float):
            # Это ошибка! Тест должен упасть
            self.fail("Найдена ошибка: параметры amount и category перепутаны в Expense.__init__!")
        else:
            # Всё правильно — тест проходит
            self.assertIsInstance(expense.amount, (int, float))
            self.assertIsInstance(expense.category, str)