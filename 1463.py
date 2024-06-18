import sys
input = sys.stdin.readline
# 공부하고 다시 풀기
n = int(input())
cnt = 0
while n != 1:
    if n%3 == 0:
        n = n/3
    elif (n-1)%3 == 0:
        n = (n-1)/3
        cnt += 1
    elif n%2 == 0:
        n = n/2
    else:
        n -= 1
    cnt += 1
print(cnt)