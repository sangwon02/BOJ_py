import sys
x, y = map(int, sys.stdin.readline().split())
A = list(map(int, input().split()))

for n in range(x):
    if  A[n]< y:
        print(A[n], end=' ')