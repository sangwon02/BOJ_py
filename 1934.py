import sys
num = int(sys.stdin.readline())

for i in range(num):
    n1, n2 = map(int, sys.stdin.readline().split())
    num1, num2 = n1, n2
    while n1!=0:
        n2 = n2%n1
        n1, n2 = n2, n1   

    n = num1 * num2 //n2
    print(n)