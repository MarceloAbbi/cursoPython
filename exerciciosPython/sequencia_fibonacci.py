def fibonacci(n):
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    return n
for i in range(20):
    print(fibonacci(i))