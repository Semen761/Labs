from datetime import datetime

# Получаем текущую дату и время
now = datetime.now()

print("=== Текущая дата и время ===")
print(f"Текущая дата и время: {now}")
print(f"Только текущая дата: {now.date()}")
print(f"Только текущее время: {now.time()}")
