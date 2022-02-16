n = int(input())
n1 = int(input())
n5 = 0
n3 = 10
n4 = 1

for i in range(n):
    n2 = (n1%n3)//n4
    n3 = n3*10
    n4 = n4*10
    n5 = n5+n2

print(n5)

