import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split())) 
cnt = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if li[j] > li[i]:
            cnt[i] = max(cnt[i],cnt[j]+1)
print(max(cnt))