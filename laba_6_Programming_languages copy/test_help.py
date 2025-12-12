#!/usr/bin/env python3
"""
Тестовый скрипт для проверки документации с помощью help()
"""

import fin_app
import fin_app.commands
import fin_app.storage
import fin_app.report
import fin_app.models


def test_help():
    """Тестирует отображение документации через help()"""
    
    print("=" * 60)
    print("ТЕСТ ДОКУМЕНТАЦИИ С ПОМОЩЬЮ help()")
    print("=" * 60)
    
    # Тестируем основной пакет
    print("\n1. Документация пакета fin_app:")
    print("-" * 40)
    help(fin_app)
    
    # Тестируем модуль commands
    print("\n2. Документация модуля commands:")
    print("-" * 40)
    help(fin_app.commands)
    
    # Тестируем функции в commands
    print("\n3. Документация функции add_command:")
    print("-" * 40)
    help(fin_app.commands.add_command)
    
    print("\n4. Документация функции show_command:")
    print("-" * 40)
    help(fin_app.commands.show_command)
    
    # Тестируем модуль storage
    print("\n5. Документация модуля storage:")
    print("-" * 40)
    help(fin_app.storage)
    
    print("\n6. Документация функции add_expense:")
    print("-" * 40)
    help(fin_app.storage.add_expense)
    
    # Тестируем модуль report
    print("\n7. Документация модуля report:")
    print("-" * 40)
    help(fin_app.report)
    
    print("\n8. Документация функции make_report:")
    print("-" * 40)
    help(fin_app.report.make_report)
    
    # Тестируем модуль models
    print("\n9. Документация модуля models:")
    print("-" * 40)
    help(fin_app.models)
    
    print("\n10. Документация класса Expense:")
    print("-" * 40)
    help(fin_app.models.Expense)
    
    print("\n" + "=" * 60)
    print("ТЕСТ ЗАВЕРШЕН!")
    print("=" * 60)


def test_interactive_help():
    """Интерактивная проверка конкретных элементов"""
    print("\nИНТЕРАКТИВНАЯ ПРОВЕРКА:")
    print("Для проверки введите имя модуля/функции (или 'exit' для выхода):")
    
    while True:
        try:
            user_input = input("\n>>> ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'выход']:
                break
            elif user_input == 'fin_app':
                help(fin_app)
            elif user_input == 'commands':
                help(fin_app.commands)
            elif user_input == 'add_command':
                help(fin_app.commands.add_command)
            elif user_input == 'storage':
                help(fin_app.storage)
            elif user_input == 'add_expense':
                help(fin_app.storage.add_expense)
            elif user_input == 'report':
                help(fin_app.report)
            elif user_input == 'make_report':
                help(fin_app.report.make_report)
            elif user_input == 'models':
                help(fin_app.models)
            elif user_input == 'Expense':
                help(fin_app.models.Expense)
            elif user_input == 'Category':
                help(fin_app.models.Category)
            else:
                print("Доступные варианты: fin_app, commands, add_command, storage, add_expense, report, make_report, models, Expense, Category")
                
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    # Автоматический тест
    test_help()
    
    # Интерактивный режим
    test_interactive_help()