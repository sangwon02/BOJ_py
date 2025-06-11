import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
heap = [] 

for _ in range(n):
    x = int(input()) 
    if x!=0: 
        heappush(heap,-x)  
    else:
        if len(heap):
            print(-heappop(heap))
        else:
            print(0)