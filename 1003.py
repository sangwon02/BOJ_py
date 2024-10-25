import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    n1, n2 = 1, 0
    for i in range(n):
        n1, n2 = n2, n1 + n2
    print(n1, n2)