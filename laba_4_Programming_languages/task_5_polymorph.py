from task_1_base_class import Transport
from task_2_inheritance import Car, Bike

# Список объектов
objects = [
    Transport("Поезд", 100),
    Car("BMW", 200, 2),
    Bike("Merida", 30, "горный")
]

# Цикл
for obj in objects:
    obj.move()

print("Это полиморфизм!")
