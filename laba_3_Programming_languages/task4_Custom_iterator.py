class Countdown:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        self.current = self.n
        return self
    
    def __next__(self):
        if self.current < 1:
            raise StopIteration
        num = self.current
        self.current -= 1
        return num

# Вводим число с клавиатуры
n = int(input("Введите число: "))

# Выводим все числа в одной строке
result = []
for x in Countdown(n):
    result.append(str(x))

print("Вывод:", " ".join(result))