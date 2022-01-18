a = int(input())
b = int(input())
c = int(input())
x = a*b*c
n1 = 10
n3 = 1
list = [0,0,0,0,0,0,0,0,0,0,0]

while True:
    n2 = (x%n1)//n3
    list[n2]=list[n2]+1
    n1 = n1*10
    n3 = n3*10
    if n1>x*10:
        break
for i in range(10):
    print(list[i])