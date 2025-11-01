import json
import os
from datetime import datetime

FILE_NAME = "money.json"

def save_data(data):
    try:
        with open(FILE_NAME, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Ошибка сохранения: {e}")

def load_data():
    try:
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    except:
        return []

def add_expense(category, amount):
    data = load_data()
    
    new_item = {
        "id": len(data) + 1,
        "category": category,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    data.append(new_item)
    save_data(data)
    return new_item

def get_all_expenses():
    return load_data()