import json
import os
import csv
from datetime import datetime, timedelta

FILE_NAME_JSON = "money.json"
FILE_NAME_CSV = "money.csv"

def save_data_json(data):
    try:
        with open(FILE_NAME_JSON, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"❌ Ошибка сохранения JSON: {e}")

def save_data_csv(data):
    try:
        if data:
            # Берем только основные поля для CSV
            csv_data = []
            for item in data:
                csv_item = {
                    "id": item["id"],
                    "category": item["category"],
                    "amount": item["amount"],
                    "date": item["date"]
                }
                csv_data.append(csv_item)
            
            with open(FILE_NAME_CSV, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=csv_data[0].keys())
                writer.writeheader()
                writer.writerows(csv_data)
    except Exception as e:
        print(f"❌ Ошибка сохранения CSV: {e}")

def load_data():
    try:
        if os.path.exists(FILE_NAME_JSON):
            with open(FILE_NAME_JSON, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    except Exception as e:
        print(f"❌ Ошибка загрузки данных: {e}")
        return []

def add_expense(category, amount, description="", custom_date=None):
    try:
        data = load_data()
        
        if custom_date:
            # Парсим пользовательскую дату
            try:
                date_obj = datetime.strptime(custom_date, "%Y-%m-%d")
                date_str = date_obj.strftime("%Y-%m-%d %H:%M")
                timestamp = date_obj.isoformat()
            except ValueError:
                return None, "❌ Неправильный формат даты. Используйте: ГГГГ-ММ-ДД"
        else:
            # Используем текущую дату
            date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
            timestamp = datetime.now().isoformat()
        
        new_item = {
            "id": len(data) + 1,
            "category": category,
            "amount": amount,
            "description": description,
            "date": date_str,
            "timestamp": timestamp
        }
        
        data.append(new_item)
        save_data_json(data)
        save_data_csv(data)
        return new_item, None
    except Exception as e:
        print(f"❌ Ошибка добавления расхода: {e}")
        return None, str(e)

def get_expenses_by_period(period):
    try:
        data = load_data()
        if not data:
            return []
        
        now = datetime.now()
        filtered_data = []
        
        for item in data:
            item_date = datetime.fromisoformat(item['timestamp'])
            
            if period == 'day' and item_date.date() == now.date():
                filtered_data.append(item)
            elif period == 'month' and item_date.month == now.month and item_date.year == now.year:
                filtered_data.append(item)
            elif period == 'all':
                filtered_data.append(item)
        
        return filtered_data
    except Exception as e:
        print(f"❌ Ошибка фильтрации по периоду: {e}")
        return []

def get_all_expenses():
    try:
        return load_data()
    except Exception as e:
        print(f"❌ Ошибка загрузки всех данных: {e}")
        return []