import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'fin_app'))

import unittest
import tempfile
import os
from storage import Storage

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.test_file = tempfile.mktemp(suffix=".json")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_expense_returns_tuple(self):
        """add_expense возвращает кортеж (expense_dict, None)"""
        storage = Storage(self.test_file)
        result = storage.add_expense(1000, "Еда", "Обед")
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        expense_dict, error = result
        self.assertIsInstance(expense_dict, dict)
        self.assertIsNone(error)
        self.assertEqual(expense_dict['amount'], 1000)
        self.assertEqual(expense_dict['category'], "Еда")

    def test_get_all_expenses(self):
        """get_all_expenses возвращает все расходы"""
        storage = Storage(self.test_file)
        storage.add_expense(100, "Еда", "Хлеб")
        storage.add_expense(200, "Транспорт", "Автобус")
        expenses = storage.get_all_expenses()
        self.assertEqual(len(expenses), 2)

    def test_load_data_returns_list(self):
        """load_data возвращает список"""
        storage = Storage(self.test_file)
        data = storage.load_data()
        self.assertIsInstance(data, list)

    def test_save_and_load_consistency(self):
        """Сохранение и загрузка данных согласованы"""
        storage = Storage(self.test_file)
        storage.add_expense(1500, "Аренда", "Квартира")
        data = storage.load_data()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['amount'], 1500)
        self.assertEqual(data[0]['category'], "Аренда")