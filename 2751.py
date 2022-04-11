import sys
n = int(sys.stdin.readline())
num = []

for i in range(n):
    num.append(int(sys.stdin.readline()))

for i in sorted(num):
    print(i)