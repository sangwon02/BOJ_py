import sys

a, b = map(int, sys.stdin.readline().split())

c, d = max(a, b), min(a, b)
t = 1
while t > 0:
    t = c % d
    c, d = d, t
answer = int(a*b/c)

print(answer)
