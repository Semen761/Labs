import unittest
import sys
import os
# Добавляем путь к fin_app, чтобы избежать relative import
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'fin_app'))

from commands import add_expense_command, list_expenses_command
from storage import Storage

class TestCommandsSimple(unittest.TestCase):
    def setUp(self):
        """Создаем временный файл для тестов"""
        self.test_file = "test_expenses.json"
        with open(self.test_file, "w") as f:
            f.write("[]")

    def tearDown(self):
        """Удаляем временный файл после тестов"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_commands_simple(self):
        """Простой тест команд"""
        storage = Storage(self.test_file)
        
        # Тестируем add_expense_command
        result = add_expense_command(storage, 500, "Развлечения", "Кино")
        self.assertTrue(result.startswith("Добавлено"))
        
        # Тестируем list_expenses_command
        output = list_expenses_command(storage)
        self.assertIn("Расходы:", output)
        self.assertIn("Развлечения", output)