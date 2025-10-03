def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
print("=== Fibonacci ===")
for num in fibonacci(6):
    print(num, end=' ')
print("\n")
