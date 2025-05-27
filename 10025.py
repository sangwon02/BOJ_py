import sys
input = sys.stdin.readline


n, k = map(int, input().split())
waterbkt = []
max_sum = 0

for _ in range(n):
    waterbkt.append(list(map(int, input().split())))
waterbkt.sort(key=lambda x: x[1])

start, end, window_sum = 0, 0, 0
while start <= end and end < n:
    if waterbkt[end][1] - waterbkt[start][1] <= 2*k:
        window_sum += waterbkt[end][0]
        max_sum = max(max_sum, window_sum)
        end += 1 
    else:
        window_sum -= waterbkt[start][0]
        start += 1
print(max_sum)