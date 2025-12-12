#!/usr/bin/env python3
"""
Запуск всех тестов
"""

import unittest
import os
import sys

def run_tests():
    """Запускает все тесты"""
    print("=" * 60)
    print("ЗАПУСК ТЕСТОВ ДЛЯ ФИНАНСОВОГО ПРИЛОЖЕНИЯ")
    print("=" * 60)
    
    # Находим тесты
    test_dir = os.path.dirname(os.path.abspath(__file__))
    test_files = [
        'test_models_fixed.py',
        'test_storage_fixed.py', 
        'test_commands_simple.py',
        'test_report_simple.py'
    ]
    
    # Загружаем тесты
    loader = unittest.TestLoader()
    suites = []
    
    for test_file in test_files:
        file_path = os.path.join(test_dir, test_file)
        if os.path.exists(file_path):
            print(f"\nЗагружаю {test_file}...")
            suite = loader.discover(test_dir, pattern=test_file)
            suites.append(suite)
        else:
            print(f"⚠ Файл {test_file} не найден")
    
    # Объединяем
    combined_suite = unittest.TestSuite(suites)
    
    # Запускаем
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(combined_suite)
    
    # Статистика
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ:")
    print(f"Всего тестов: {result.testsRun}")
    print(f"Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Провалены: {len(result.failures)}")
    print(f"Ошибки: {len(result.errors)}")
    print(f"Пропущены: {len(result.skipped)}")
    
    if result.wasSuccessful():
        print("✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
    else:
        print("❌ ЕСТЬ ПРОБЛЕМЫ!")
    print("=" * 60)
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)