from decimal import Decimal

print("=== Калькулятор вкладов ===")

# Вводим данные
summa = Decimal(input("Сумма вклада: "))
procent = Decimal(input("Процент годовых: "))
srok = Decimal(input("Срок в годах: "))

# Считаем по формуле
mes_procent = procent / Decimal('100') / Decimal('12')
mesyacev = srok * Decimal('12')

itog = summa * (1 + mes_procent) ** mesyacev
itog = itog.quantize(Decimal('0.01'))

pribyl = itog - summa

# Выводим результат
print(f"Итог: {itog} руб.")
print(f"Прибыль: {pribyl} руб.")