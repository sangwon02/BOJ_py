import sys
input = sys.stdin.readline


N, M = map(int, input().split())

li = list(map(int, input().split()))

sum_li = [0]

for i in range(N):
    sum_li.append(sum_li[-1] + li[i])
    
for i in range(M):
    i, j = map(int, input().split())
    
    print(sum_li[j]-sum_li[i-1])
    