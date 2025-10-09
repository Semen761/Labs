def countdown(n):
    current = n
    while current >= 1:
        yield current
        current -= 1

# Ввод числа от пользователя
n = int(input("Введите число для обратного отсчета: "))

# Обратный отсчет
print(f"Обратный отсчет от {n}:")
for x in countdown(n):
    print(x, end=" ")

print() 