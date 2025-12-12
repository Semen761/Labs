"""
Модуль обработки команд пользователя.

Этот модуль содержит функции для выполнения различных команд,
связанных с управлением расходами.
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import storage
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'fin_app'))

import unittest
import tempfile
import os
from commands import add_expense_command, list_expenses_command
from storage import Storage

class TestCommandsSimple(unittest.TestCase):
    def setUp(self):
        self.test_file = tempfile.mktemp(suffix=".json")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_commands_simple(self):
        """Простой тест команд"""
        storage = Storage(self.test_file)
        msg = add_expense_command(storage, 500, "Развлечения", "Кино")
        self.assertIn("Добавлено", msg)

        output = list_expenses_command(storage)
        self.assertIn("500", output)
        self.assertIn("Развлечения", output)


def add_expense_command(storage, amount, category, description):
    expense, error = storage.add_expense(amount, category, description)
    if error:
        return f"Ошибка: {error}"
    return f"Добавлено: {expense['amount']} руб. на {expense['category']}"

def list_expenses_command(storage):
    expenses = storage.get_all_expenses()
    if not expenses:
        return "Расходы отсутствуют."
    lines = ["Расходы:"]
    for e in expenses:
        lines.append(f"- {e['amount']} руб. на {e['category']}: {e['description']}")
    return "\n".join(lines)
  
def add_command(category, amount, description="", date=None):
    """Добавляет новый расход.

    Args:
        category (str): Категория расхода (например, 'еда', 'транспорт')
        amount (float): Сумма расхода
        description (str, optional): Описание расхода. По умолчанию "".
        date (str, optional): Дата в формате 'ГГГГ-ММ-ДД'. По умолчанию None.

    Returns:
        bool: True если расход успешно добавлен, False в противном случае
    """
    try:
        result, error = storage.add_expense(category, amount, description, date)
        if result:
            return True
        else:
            print(error if error else "❌ Не удалось добавить расход")
            return False
    except Exception as e:
        print(f"❌ Ошибка выполнения команды добавления: {e}")
        return False


def delete_command(expense_id):
    """Удаляет расход по идентификатору.

    Args:
        expense_id (int): ID расхода для удаления

    Returns:
        bool: True если расход успешно удален, False в противном случае
    """
    try:
        success, error = storage.delete_expense(expense_id)
        if not success:
            print(error if error else "❌ Не удалось удалить расход")
        return success
    except Exception as e:
        print(f"❌ Ошибка выполнения команды удаления: {e}")
        return False


def show_categories_command():
    """Показывает все существующие категории расходов."""
    try:
        categories = storage.get_all_categories()
        if not categories:
            print("📭 Категорий нет")
            return
        
        print("\n🏷️  ВСЕ КАТЕГОРИИ:")
        print("-" * 30)
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        print(f"\nВсего категорий: {len(categories)}")
        
    except Exception as e:
        print(f"❌ Ошибка показа категорий: {e}")


def show_command(period='all', category=None):
    """Показывает расходы за указанный период и/или категорию.

    Args:
        period (str, optional): Период ('day', 'month', 'all'). По умолчанию 'all'.
        category (str, optional): Фильтр по категории. По умолчанию None.
    """
    try:
        data = storage.get_expenses_by_period(period, category)
        
        if not data:
            if category:
                print(f"📭 Записей за {period} в категории '{category}' нет")
            else:
                print(f"📭 Записей за {period} нет")
            return
        
        period_names = {
            'day': 'ДЕНЬ',
            'month': 'МЕСЯЦ', 
            'all': 'ВСЕ'
        }
        
        if category:
            print(f"\n📋 РАСХОДЫ ЗА {period_names[period]} (категория: {category}):")
        else:
            print(f"\n📋 РАСХОДЫ ЗА {period_names[period]}:")
        
        print("-" * 50)
        
        total = 0
        for item in data:
            print(f"№{item['id']} | {item['date']}")
            print(f"   🏷️  {item['category']}: {item['amount']} руб.")
            if item.get('description'):
                print(f"   📝 {item['description']}")
            print()
            total += item['amount']
        
        if category:
            print(f"💰 ИТОГО за {period_names[period]} в категории '{category}': {total} руб.")
        else:
            print(f"💰 ИТОГО за {period_names[period]}: {total} руб.")
        
    except Exception as e:
        print(f"❌ Ошибка показа расходов: {e}")


def report_command(period='all'):
    """Генерирует отчет за указанный период.

    Args:
        period (str, optional): Период для отчета ('day', 'month', 'all'). По умолчанию 'all'.

    Returns:
        bool: True если отчет успешно сгенерирован, False в противном случае
    """
    try:
        success = report.make_report(period)
        if not success:
            print(f"❌ Не удалось сгенерировать отчет за {period}")
        return success
    except Exception as e:
        print(f"❌ Ошибка генерации отчета: {e}")
        return False
      
      
# НИКАКИХ импортов самого себя!
# НИКАКИХ sys.path!
# Только функции, которые принимают storage как аргумент

def add_expense_command(storage, amount, category, description):
    expense, error = storage.add_expense(amount, category, description)
    if error:
        return f"Ошибка: {error}"
    return f"Добавлено: {expense['amount']} руб. на {expense['category']}"

def list_expenses_command(storage):
    expenses = storage.get_all_expenses()
    if not expenses:
        return "Расходы отсутствуют."
    lines = ["Расходы:"]
    for e in expenses:
        lines.append(f"- {e['amount']} руб. на {e['category']}: {e['description']}")
    return "\n".join(lines)