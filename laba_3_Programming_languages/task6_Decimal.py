from decimal import Decimal

print("=== Калькулятор вкладов ===")

# Вводим данные с автоматическим исправлением запятых на точки
summa_input = input("Сумма вклада (руб.коп): ").replace(',', '.')
summa = Decimal(summa_input)

procent_input = input("Процент годовых: ").replace(',', '.')
procent = Decimal(procent_input)

srok_input = input("Срок в годах: ").replace(',', '.')
srok = Decimal(srok_input)

# Считаем по формуле
mes_procent = procent / Decimal('100') / Decimal('12')
mesyacev = srok * Decimal('12')

itog = summa * (1 + mes_procent) ** mesyacev
itog = itog.quantize(Decimal('0.01'))

pribyl = itog - summa
pribyl = pribyl.quantize(Decimal('0.01'))

# Выводим результат
print(f"\nРезультаты расчета:")
print(f"Начальная сумма: {summa} руб.")
print(f"Процент годовых: {procent}%")
print(f"Срок вклада: {srok} лет")
print(f"Итоговая сумма: {itog} руб.")
print(f"Прибыль: {pribyl} руб.")

# Дополнительный вывод в копейках
itog_kop = itog * 100
pribyl_kop = pribyl * 100
print(f"\nВ копейках:")
print(f"Итог: {itog_kop:.0f} коп.")
print(f"Прибыль: {pribyl_kop:.0f} коп.")