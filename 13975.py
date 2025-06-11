import sys
from heapq import heappush, heappop
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    heap = []
    result = 0
    k = int(input())
    li = list(map(int, input().split()))
    for i in li:
        heappush(heap, i)
    while len(heap) != 1:
        num1 = heappop(heap)
        num2 = heappop(heap)
        result += num1 + num2
        heappush(heap, num1+num2)
    print(result)
