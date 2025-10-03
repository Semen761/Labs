from datetime import datetime
def format_date_ru(dt):
    months = [
        'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
        'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'
    ]
    return f"Сегодня {dt.day} {months[dt.month-1]} {dt.year} года, время: {dt:%H:%M}"
now = datetime.now()
print(format_date_ru(now))
