import argparse
from fin_app import commands

def main():
    parser = argparse.ArgumentParser(description='Финансовый трекер расходов')
    
    # Команда добавления
    parser.add_argument('--add', help='Добавить расход (название категории)')
    parser.add_argument('--sum', type=float, help='Сумма расхода')
    parser.add_argument('--date', help='Дата расхода (формат: ГГГГ-ММ-ДД)')
    parser.add_argument('--desc', help='Описание расхода')
    
    # Команда просмотра с периодами
    parser.add_argument('--show', choices=['day', 'month', 'all'], help='Показать расходы за период')
    
    # Команда отчета с периодами
    parser.add_argument('--report', choices=['day', 'month', 'all'], help='Сделать отчет за период')
    
    args = parser.parse_args()
    
    try:
        if args.add and args.sum:
            commands.add_command(args.add, args.sum, args.desc, args.date)
            if args.date:
                print(f"✅ Добавлено: {args.add} - {args.sum} руб. (дата: {args.date})")
            else:
                print(f"✅ Добавлено: {args.add} - {args.sum} руб.")
            
        elif args.show:
            commands.show_command(args.show)
            
        elif args.report:
            commands.report_command(args.report)
            
        else:
            print("💡 Как использовать:")
            print("  Добавить (сегодня): python main.py --add 'еда' --sum 250")
            print("  Добавить (с датой): python main.py --add 'еда' --sum 250 --date 2024-01-15")
            print("  Показать: python main.py --show day/month/all")
            print("  Отчет:    python main.py --report day/month/all")
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    main()