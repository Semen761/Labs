from . import storage
from . import report

def add_command(category, amount, description="", date=None):
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

def show_command(period='all'):
    try:
        data = storage.get_expenses_by_period(period)
        
        if not data:
            print(f"📭 Записей за {period} нет")
            return
        
        period_names = {
            'day': 'ДЕНЬ',
            'month': 'МЕСЯЦ', 
            'all': 'ВСЕ'
        }
        
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
        
        print(f"💰 ИТОГО за {period_names[period]}: {total} руб.")
        
    except Exception as e:
        print(f"❌ Ошибка показа расходов: {e}")

def report_command(period='all'):
    try:
        success = report.make_report(period)
        if not success:
            print(f"❌ Не удалось сгенерировать отчет за {period}")
    except Exception as e:
        print(f"❌ Ошибка генерации отчета: {e}")