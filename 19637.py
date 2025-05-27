import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
title = []

for i in range(n):
    title.append(input().split())
 
for i in range(m):
    character = int(input())
    idx = 0
    start, end = 0, len(title)-1
    while start <= end:
        mid = (start + end) // 2
        if int(title[mid][1]) < character:
            start = mid + 1
        else:
            idx = mid
            end = mid - 1
    print(title[idx][0])
 
