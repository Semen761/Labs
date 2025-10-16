# 1. Базовый класс
class Transport:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    
    def move(self):
        print(f"Transport is moving at {self.speed} km/h")
    
    def __str__(self):
        return f"Transport: {self.brand}, Speed: {self.speed}"

# Проверка
if __name__ == "__main__":
    t = Transport("Audi", 100)
    print(t)
    t.move()
