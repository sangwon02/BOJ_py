n = int(input())

for i in range(n):
    a = int(input())
    b = int(str(a)[::-1])
    c = a + b
    if c == int(str(c)[::-1]):
        print("YES")
    else:
        print("NO")