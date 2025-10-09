def fibonacci(n):
    a, b = 0, 1
    nums = []
    for i in range(n):
        nums.append(str(a))
        a, b = b, a+b
    return " ".join(nums)

n = int(input("Введите кол-во чисел фибоначи: "))
print(fibonacci(n))