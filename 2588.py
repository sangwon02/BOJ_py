x = int(input())
y = int(input())

x1 = int(y%10)
x2 = int((y%100)//10)
x3 = int(y//100)


print(x*x1)
print(x*x2)
print(x*x3)
print(x*y)