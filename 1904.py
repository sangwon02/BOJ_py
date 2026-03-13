import sys
input = sys.stdin.readline
n = int(input())

li = [0] * (n + 1) 

li[1] = 1 

if n > 1:
    li[2] = 2
for i in range(3, n+1):
    li[i] = (li[i - 1] + li[i - 2]) % 15746 

print(li[n])