from datetime import datetime

def format_datetime_ru(dt):
    """
    Форматирует datetime в строку на русском языке
    Формат: "Сегодня 26 сентября 2025 года, время: 05:30"
    """
    # Словарь месяцев на русском
    months = {
        1: "января", 2: "февраля", 3: "марта", 4: "апреля",
        5: "мая", 6: "июня", 7: "июля", 8: "августа",
        9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
    }
    
    day = dt.day
    month = months[dt.month]
    year = dt.year
    time_str = dt.strftime("%H:%M")
    
    return f"Сегодня {day} {month} {year} года, время: {time_str}"

# Пример использования
current_time = datetime.now()
formatted_string = format_datetime_ru(current_time)
print(formatted_string)

# Тестируем с конкретной датой как в примере
test_date = datetime(2025, 9, 26, 5, 30)
test_formatted = format_datetime_ru(test_date)
print(f"\\nТест с датой из примера: {test_formatted}")
