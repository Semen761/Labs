from datetime import date
birth_date = date(1995, 8, 20)
today = date.today()
days_passed = (today - birth_date).days
next_birthday = date(today.year, birth_date.month, birth_date.day)
if next_birthday < today:
    next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
days_to_birthday = (next_birthday - today).days
print(f"Дата рождения: {birth_date}")
print(f"Сегодня: {today}")
print(f"Дней прошло с рождения: {days_passed}")
print(f"Дней до следующего дня рождения: {days_to_birthday}")
