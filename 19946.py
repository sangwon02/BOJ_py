N = int(input())
cnt = 64

while N % 2 == 0:
    N //= 2
    cnt -= 1

print(cnt)