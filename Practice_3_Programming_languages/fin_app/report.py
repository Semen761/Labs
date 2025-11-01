from . import storage

def make_report():
    data = storage.load_data()
    
    if not data:
        print("😴 Нет данных для отчета")
        return
    
    categories = {}
    total = 0
    
    for item in data:
        cat = item["category"]
        amount = item["amount"]
        
        if cat not in categories:
            categories[cat] = 0
        categories[cat] += amount
        total += amount
    
    print("\n" + "="*30)
    print("ОТЧЕТ ПО РАСХОДАМ")
    print("="*30)
    
    for cat, amount in categories.items():
        print(f"🏷️  {cat}: {amount} руб.")
    
    print(f"💰 ВСЕГО: {total} руб.")
    print("="*30)
    
    try:
        with open("report.txt", "w", encoding='utf-8') as f:
            f.write("ОТЧЕТ ПО РАСХОДАМ\n")
            f.write("="*30 + "\n")
            for cat, amount in categories.items():
                f.write(f"{cat}: {amount} руб.\n")
            f.write("="*30 + "\n")
            f.write(f"ОБЩАЯ СУММА: {total} руб.\n")
        print("💾 Отчет сохранен в report.txt")
    except Exception as e:
        print(f"❌ Не смог сохранить файл: {e}")