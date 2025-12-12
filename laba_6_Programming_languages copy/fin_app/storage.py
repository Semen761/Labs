class Storage:
    def __init__(self, filepath="expenses.json"):
        self.filepath = filepath
        self._ensure_file()

    def _ensure_file(self):
        import os, json
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w") as f:
                json.dump([], f)

    def add_expense(self, amount, category, description, date=None):
        # ... как раньше ...
        pass

    def get_all_expenses(self):
        # ...
        pass

# Также должны быть глобальные функции (используются в commands.py):
def add_expense(amount, category, description, date=None):
    # оборачивает Storage
    pass

def get_expenses_by_period(period, category=None):
    # ...
    pass

def get_all_categories():
    # ...
    pass
  
import json
import os
from datetime import datetime

class Storage:
    def __init__(self, filepath="expenses.json"):
        self.filepath = filepath
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump([], f)

    def load_data(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_data(self, data):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def add_expense(self, amount, category, description):
        data = self.load_data()
        new_id = max([e.get("id", 0) for e in data], default=0) + 1
        expense = {
            "id": new_id,
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "timestamp": datetime.now().isoformat()
        }
        data.append(expense)
        self.save_data(data)
        return expense, None

    def get_all_expenses(self):
        return self.load_data()