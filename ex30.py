x = int(input())
e = x
f = 0

while True:
    a = e//10
    b = e%10
    c = (a+b)%10
    e = b*10 + c
    f = f + 1
    if e == x:
        break

print(f)