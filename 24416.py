def fib(n):
    global fibnum
    if n == 1 or n == 2:
        fibnum += 1    
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    global fibonaccinum
    f = [0] * (n + 1)
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        fibonaccinum += 1    
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


fibnum = 0
fibonaccinum = 0
n = int(input())
fib(n)
fibonacci(n)
print(fibnum, fibonaccinum)