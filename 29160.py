import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, k = map(int, input().split())

heap = []

for _ in range(11):
    heap.append([])


for _ in range(n):
    p, w = map(int, input().split())
    heappush(heap[p-1], -w)

for _ in range(k):
    for i in range(11):
        if len(heap[i]):
            num = -heappop(heap[i]) - 1
            if num == -1:
                num = 0
            heappush(heap[i], -num)

num = 0
for i in range(11):
    if len(heap[i]):
        num += -heappop(heap[i])
print(num)