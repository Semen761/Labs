from task_1_base_class import Transport

class Car(Transport):
    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats
    
    def honk(self):
        print("Beep beep!")
    
    def move(self):
        print(f"Car {self.brand} is driving at {self.speed} km/h")
    
    def __str__(self):
        return f"Car: {self.brand}, Speed: {self.speed}, Seats: {self.seats}"

class Bike(Transport):
    def __init__(self, brand, speed, type):
        super().__init__(brand, speed)
        self.type = type
    
    def move(self):
        print(f"Bike {self.brand} is cycling at {self.speed} km/h")
    
    def __str__(self):
        return f"Bike: {self.brand}, Speed: {self.speed}, Type: {self.type}"

# Проверка
if __name__ == "__main__":
    car = Car("Toyota", 120, 5)
    bike = Bike("Giant", 25, "mountain")
    print(car)
    print(bike)
    car.move()
    bike.move()
    car.honk()
