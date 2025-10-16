# Импортируем классы из других файлов
from task_1_base_class import Transport

# Создаем свои классы с нужными методами
class Car(Transport):
    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats
    
    def honk(self):
        print("Би-бип!")
    
    def __str__(self):
        return f"Машина {self.brand} со скоростью {self.speed} км/ч"
    
    def __len__(self):
        return self.seats  # Теперь len() будет работать!
    
    def __eq__(self, other):
        if isinstance(other, Car):
            return self.speed == other.speed
        return False
    
    def __add__(self, other):
        if isinstance(other, Car):
            return self.speed + other.speed
        else:
            return "Нельзя сложить с этим объектом!"

class Bike(Transport):
    def __init__(self, brand, speed, bike_type):
        super().__init__(brand, speed)
        self.bike_type = bike_type
    
    def ring_bell(self):
        print("Дзинь-дзинь!")
    
    def __str__(self):
        return f"Велосипед {self.brand} со скоростью {self.speed} км/ч"


# 1. Создаем объекты разных классов
автобус = Transport("Автобус", 60)
машина1 = Car("Toyota", 120, 5)
машина2 = Car("Honda", 130, 4)
велосипед = Bike("Stels", 25, "городской")

# 2. Выводим их на экран
print("\n1. Выводим объекты:")
print(автобус)
print(машина1)
print(машина2)
print(велосипед)

# 3. Проверяем методы move() и honk()
print("\n2. Проверяем методы:")
машина1.move()      # Должно работать из Transport
велосипед.move()    # Должно работать из Transport
машина1.honk()      # Должно работать из Car

# 4. Используем len() для машины 
print("\n3. Используем len():")
print(f"В машине {машина1.brand} мест: {len(машина1)}")
print(f"В машине {машина2.brand} мест: {len(машина2)}")

# 5. Сравниваем две машины
print("\n4. Сравниваем машины:")
print(f"Скорости машин одинаковые? {машина1 == машина2}")

# 6. Складываем скорости двух машин
print("\n5. Складываем скорости:")
общая_скорость = машина1 + машина2
print(f"Сумма скоростей: {общая_скорость} км/ч")

# 7. Пробуем сложить машину и велосипед
print("\n6. Пробуем сложить машину и велосипед:")
результат = машина1 + велосипед
print(f"Результат: {результат}")
print("Почему ошибка? Потому что машина умеет складываться только с другой машиной!")
