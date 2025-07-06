import sys
import heapq
input = sys.stdin.readline

heap = []
n = int(input())

for _ in range(n):
    li = map(int, input().split())
    
    for number in li:
        if len(heap) < n: 
            heapq.heappush(heap, number)
            
        else:
            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
print(heap[0])