import argparse
from fin_app import commands

def main():
    parser = argparse.ArgumentParser(description='Финансовый трекер')
    
    parser.add_argument('--add', help='Добавить расход')
    parser.add_argument('--sum', type=float, help='Сумма расхода')
    parser.add_argument('--show', action='store_true', help='Показать все')
    parser.add_argument('--report', action='store_true', help='Сделать отчет')
    
    args = parser.parse_args()
    
    try:
        if args.add and args.sum:
            commands.add_command(args.add, args.sum)
            print(f"✅ Добавлено: {args.add} - {args.sum} руб.")
            
        elif args.show:
            commands.show_command()
            
        elif args.report:
            commands.report_command()
            
        else:
            print("💡 Как использовать:")
            print("  Добавить: python main.py --add 'еда' --sum 250")
            print("  Показать: python main.py --show")
            print("  Отчет:    python main.py --report")
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    main()