import sys
input = sys.stdin.readline
from collections import deque

n, s = map(int, input().split())
nums = list(map(int, input().split()))

queue = deque()
current_sum = 0
minnum = 99999999

for num in nums:
    queue.append(num)
    current_sum += num
    
    while current_sum >= s:
        length = len(queue)
        
        if length < minnum:
            minnum = length
            
        current_sum -= queue.popleft()

if minnum == 99999999:
    print(0)
else:
    print(minnum)
