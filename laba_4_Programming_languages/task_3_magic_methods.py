from task_2_inheritance import Car

class CarWithMagic(Car):
    def __len__(self):
        return self.seats
    
    def __eq__(self, other):
        return self.speed == other.speed
    
    def __add__(self, other):
        return self.speed + other.speed

# Проверка
if __name__ == "__main__":
    car1 = CarWithMagic("Toyota", 120, 5)
    car2 = CarWithMagic("Honda", 130, 4)
    
    print(f"Мест в машине: {len(car1)}")
    print(f"Скорости равны: {car1 == car2}")
    print(f"Сумма скоростей: {car1 + car2}")
