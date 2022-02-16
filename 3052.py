num = []
num1 = []
for n in range(10):
    a = int(input())
    num.append(a)
    num[n] = num[n]%42
for v in num:
    if v not in num1:
        num1.append(v)

print(int(len(num1)))
    
