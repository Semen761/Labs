"""
Модуль обработки команд пользователя.

Этот модуль содержит функции для выполнения различных команд,
связанных с управлением расходами.
"""

from . import storage
from . import report


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