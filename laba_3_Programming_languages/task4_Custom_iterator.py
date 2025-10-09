class Countdown:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        self.current = self.n
        return self
    
    def __next__(self):
        if self.current < 1:
            raise StopIteration
        number = self.current
        self.current -= 1
        return number

# Ввод числа от пользователя
n = int(input("Введите число для обратного отсчета: "))

# Обратный отсчет
print(f"Обратный отсчет от {n}:")
for x in Countdown(n):
    print(x, end=" ")

print()