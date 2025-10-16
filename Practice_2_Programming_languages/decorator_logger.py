def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} вернула {result}")
        print("---")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

@logger
def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

@logger
def greet(name):
    return f"Привет, {name}!"

print("Тестируем функцию add:")
add(5, 3)

print("Тестируем функцию divide:")
divide(10, 2)

print("Тестируем деление на ноль:")
divide(10, 0)

print("Тестируем функцию greet:")
greet("Вася")

print("=== ЧАСТЬ 1 ЗАВЕРШЕНА ===")
