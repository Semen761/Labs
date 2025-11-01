import json
from datetime import datetime

def fix_timestamps():
    try:
        with open('money.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for item in data:
            if 'timestamp' not in item:
                # Создаем timestamp из существующей даты
                date_str = item['date']
                try:
                    date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                    item['timestamp'] = date_obj.isoformat()
                except:
                    # Если не получается, используем текущее время
                    item['timestamp'] = datetime.now().isoformat()
        
        with open('money.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print("✅ Данные исправлены!")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    fix_timestamps()