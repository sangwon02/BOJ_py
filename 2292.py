import sys
input = sys.stdin.readline

n = int(input())

cnt = 1
tmp = 1

while True:
    if n <= 1:
        break
    n -= 6*cnt
    cnt += 1

print(cnt)