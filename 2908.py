import sys

x, y = map(int, sys.stdin.readline().split())

num1 = x//100 + ((x%100)//10)*10 + (x%10)*100
num2 = y//100 + ((y%100)//10)*10 + (y%10)*100

if num1>num2:
    print(num1)
else:
    print(num2)

    