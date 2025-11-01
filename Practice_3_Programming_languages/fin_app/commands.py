from . import storage
from . import report

def add_command(category, amount):
    storage.add_expense(category, amount)

def show_command():
    data = storage.get_all_expenses()
    
    if not data:
        print("📭 Записей нет")
        return
    
    print("\n📋 ВСЕ РАСХОДЫ:")
    print("-" * 40)
    for item in data:
        print(f"№{item['id']} | {item['date']}")
        print(f"   {item['category']}: {item['amount']} руб.")
        print()

def report_command():
    report.make_report()