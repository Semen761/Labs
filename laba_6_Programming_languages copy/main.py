"""
Главный модуль финансового трекера.

Предоставляет интерфейс командной строки для управления расходами.
Использует argparse для обработки аргументов командной строки.
"""

import argparse
from fin_app import commands

def main():
    parser = argparse.ArgumentParser(description='Финансовый трекер расходов')
    
    # Команда добавления
    parser.add_argument('--add', help='Добавить расход (название категории)')
    parser.add_argument('--sum', type=float, help='Сумма расхода')
    parser.add_argument('--date', help='Дата расхода (формат: ГГГГ-ММ-ДД)')
    parser.add_argument('--desc', help='Описание расхода')
    
    # Команда просмотра с периодами и категориями
    parser.add_argument('--show', choices=['day', 'month', 'all'], help='Показать расходы за период')
    parser.add_argument('--category', help='Показать расходы только этой категории')
    
    # Команда отчета с периодами
    parser.add_argument('--report', choices=['day', 'month', 'all'], help='Сделать отчет за период')
    
    # Команда удаления
    parser.add_argument('--delete', type=int, help='Удалить запись по ID')
    
    # Команда списка категорий
    parser.add_argument('--categories', action='store_true', help='Показать все категории')
    
    args = parser.parse_args()
    
    try:
        # УДАЛЕНИЕ ЗАПИСИ
        if args.delete:
            if commands.delete_command(args.delete):
                print(f"✅ Запись #{args.delete} удалена!")
            else:
                print(f"❌ Запись #{args.delete} не найдена")
            
        # ДОБАВЛЕНИЕ РАСХОДА
        elif args.add and args.sum:
            commands.add_command(args.add, args.sum, args.desc, args.date)
            if args.date:
                print(f"✅ Добавлено: {args.add} - {args.sum} руб. (дата: {args.date})")
            else:
                print(f"✅ Добавлено: {args.add} - {args.sum} руб.")
            
        # ПОКАЗАТЬ КАТЕГОРИИ
        elif args.categories:
            commands.show_categories_command()
            
        # ПОКАЗАТЬ РАСХОДЫ (С ФИЛЬТРАЦИЕЙ ПО ПЕРИОДУ И/ИЛИ КАТЕГОРИИ)
        elif args.show or args.category:
            period = args.show if args.show else 'all'
            category = args.category if args.category else None
            commands.show_command(period, category)
            
        # СДЕЛАТЬ ОТЧЕТ
        elif args.report:
            commands.report_command(args.report)
            
        # СПРАВКА
        else:
            print("💡 Как использовать:")
            print("  Добавить:      python main.py --add 'еда' --sum 250")
            print("  Добавить с датой: python main.py --add 'еда' --sum 250 --date 2024-01-15")
            print("  Показать:      python main.py --show day/month/all")
            print("  По категории:  python main.py --category 'еда'")
            print("  Показать+категория: python main.py --show month --category 'транспорт'")
            print("  Категории:     python main.py --categories")
            print("  Отчет:         python main.py --report day/month/all")
            print("  Удалить:       python main.py --delete 1")
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    main()