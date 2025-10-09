from datetime import datetime

now = datetime.now()
print("=== Текущая дата и время ===")
print(f"Полная дата и время: {now}")
print(f"Только дата: {now.date()}")
print(f"Только время: {now.time().strftime('%H:%M:%S')}")