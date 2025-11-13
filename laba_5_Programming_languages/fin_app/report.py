"""
Модуль генерации отчетов.

Предоставляет функциональность для создания различных типов отчетов
по расходам в разных форматах (текст, JSON, CSV).
"""


from . import storage
import csv
import json
from datetime import datetime

def make_report(period):

    """Создает отчет по расходам за указанный период.

    Генерирует отчет в трех форматах: текстовый, JSON и CSV.
    Отчет включает статистику по категориям и общую сумму.

    Args:
        period (str): Период для отчета ('day', 'month', 'all')

    Returns:
        bool: True если отчет успешно создан, False в противном случае
    """

    try:
        data = storage.get_expenses_by_period(period)
        
        if not data:
            print(f"😴 Нет данных для отчета за {period}")
            return False
        
        # Считаем по категориям
        categories = {}
        total = 0
        
        for item in data:
            cat = item["category"]
            amount = item["amount"]
            
            if cat not in categories:
                categories[cat] = 0
            categories[cat] += amount
            total += amount
        
        # Показываем на экране
        print(f"\n" + "="*35)
        print(f"📊 ОТЧЕТ ЗА {period.upper()}")
        print("="*35)
        
        for cat, amount in categories.items():
            print(f"🏷️  {cat}: {amount} руб.")
        
        print(f"💰 ВСЕГО: {total} руб.")
        print("="*35)
        
        # Сохраняем в текстовый файл
        try:
            filename_txt = f"report_{period}.txt"
            with open(filename_txt, "w", encoding='utf-8') as f:
                f.write(f"ОТЧЕТ ПО РАСХОДАМ ({period})\n")
                f.write("="*35 + "\n")
                for cat, amount in categories.items():
                    f.write(f"{cat}: {amount} руб.\n")
                f.write("="*35 + "\n")
                f.write(f"ОБЩАЯ СУММА: {total} руб.\n")
                f.write(f"Дата генерации: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            print(f"💾 Текстовый отчет сохранен в {filename_txt}")
        except Exception as e:
            print(f"❌ Ошибка сохранения текстового отчета: {e}")
        
        # Сохраняем в JSON файл
        try:
            filename_json = f"report_{period}.json"
            report_data = {
                "period": period,
                "generated_at": datetime.now().isoformat(),
                "categories": categories,
                "total": total,
                "transactions_count": len(data)
            }
            with open(filename_json, "w", encoding='utf-8') as f:
                json.dump(report_data, f, ensure_ascii=False, indent=2)
            print(f"💾 JSON отчет сохранен в {filename_json}")
        except Exception as e:
            print(f"❌ Ошибка сохранения JSON отчета: {e}")
        
        # Сохраняем в CSV файл
        try:
            filename_csv = f"report_{period}.csv"
            with open(filename_csv, "w", encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Категория", "Сумма", "Период"])
                for cat, amount in categories.items():
                    writer.writerow([cat, amount, period])
                writer.writerow(["ОБЩАЯ СУММА", total, period])
            print(f"💾 CSV отчет сохранен в {filename_csv}")
        except Exception as e:
            print(f"❌ Ошибка сохранения CSV отчета: {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка генерации отчета: {e}")
        return False