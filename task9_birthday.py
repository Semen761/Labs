from datetime import date

def calculate_birthday_info(birth_year, birth_month, birth_day):
    """
    Вычисляет сколько дней прошло с рождения и сколько дней до следующего дня рождения
    """
    # Создаем дату рождения
    birth_date = date(birth_year, birth_month, birth_day)
    today = date.today()
    
    # Дни с момента рождения
    days_since_birth = (today - birth_date).days
    
    # Следующий день рождения
    next_birthday = date(today.year, birth_month, birth_day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, birth_month, birth_day)
    
    days_to_next_birthday = (next_birthday - today).days
    
    return days_since_birth, days_to_next_birthday

# Пример использования (замените на свою дату рождения!)
birth_year = 2000
birth_month = 5
birth_day = 15

days_since, days_to = calculate_birthday_info(birth_year, birth_month, birth_day)

print("=== Разница дат ===")
print(f"Дата рождения: {birth_day:02d}.{birth_month:02d}.{birth_year}")
print(f"Сегодняшняя дата: {today}")
print(f"Дней прошло с момента рождения: {days_since}")
print(f"Дней до следующего дня рождения: {days_to}")
