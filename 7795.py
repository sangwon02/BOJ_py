import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    Ali = []
    Bli = []
    n, m = map(int, input().split())
    Ali = list(map(int, input().split()))
    Bli = list(map(int, input().split()))
    cnt = 0
    count = 0
    Ali.sort(reverse=False)
    Bli.sort(reverse=False)
    for i in range(n):
        while True:
            if count == m or Ali[i] <= Bli[count]:
                cnt += count
                break
            else:
                count += 1

    print(cnt)