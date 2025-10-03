from decimal import Decimal

def calculate_deposit():
    P = Decimal('50000.75')
    r = Decimal('5.5')
    t = Decimal('3')
    
    S = P * (1 + r/1200) ** (12 * t)
    S = S.quantize(Decimal('0.01'))
    profit = S - P
    
    print(f"Начальная сумма: {P} руб.")
    print(f"Итоговая сумма: {S} руб.")
    print(f"Прибыль: {profit} руб.")

calculate_deposit()
