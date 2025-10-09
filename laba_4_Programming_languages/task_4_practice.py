from task_1_base_class import Transport
from task_2_inheritance import Car, Bike

print("=== ПРАКТИКА ===")

# Создаем объекты
t1 = Transport("Автобус", 60)
c1 = Car("Toyota", 120, 5)
c2 = Car("Honda", 130, 4)
b1 = Bike("Stels", 25, "городской")

# Выводим
print(t1)
print(c1)
print(c2)
print(b1)

# Методы
c1.move()
b1.move()
c1.honk()

# len и сравнение
print(f"Мест: {len(c1)}")
print(f"Скорости равны: {c1 == c2}")

# Сложение
print(f"Сумма скоростей: {c1 + c2}")

# Ошибка
try:
    c1 + b1
except:
    print("Ошибка: нельзя сложить!")
