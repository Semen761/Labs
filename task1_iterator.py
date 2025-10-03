class Countdown:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        self.current = self.n
        return self
    
    def __next__(self):
        if self.current == 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

print("=== Countdown ===")
for x in Countdown(5):
    print(x, end=' ')
print("\n")
