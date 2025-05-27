import sys
input = sys.stdin.readline

n = int(input())
num = []

for i in range(n):
    num.append(int(input()))

d = [0]*n

d[0] = num[0]
if n > 1:
    d[1] = num[0]+num[1]
if n > 2:
    d[2] = max(num[2]+num[1], num[2]+num[0], d[1])

for i in range(3, n):
        d[i] = max(d[i-1], d[i-3]+num[i-1]+num[i], d[i-2]+num[i])

print(d[n-1])