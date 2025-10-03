from fractions import Fraction

# Создаем дроби 3/4 и 5/6
frac1 = Fraction(3, 4)
frac2 = Fraction(5, 6)

print("=== Дроби ===")
print(f"Дробь 1: {frac1}")
print(f"Дробь 2: {frac2}")

# Выполняем операции
addition = frac1 + frac2
subtraction = frac1 - frac2
multiplication = frac1 * frac2
division = frac1 / frac2

print("\n=== Результаты операций ===")
print(f"Сложение: {frac1} + {frac2} = {addition}")
print(f"Вычитание: {frac1} - {frac2} = {subtraction}")
print(f"Умножение: {frac1} * {frac2} = {multiplication}")
print(f"Деление: {frac1} / {frac2} = {division}")
