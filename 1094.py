
import sys
input = sys.stdin.readline

x = int(input())

sticks = [64, 32, 16, 8, 4, 2, 1]
cnt = 0

for i in range(len(sticks)):
    if x >= sticks[i]:
        cnt += 1
        x -= sticks[i]

    if x == 0:
        break

print(cnt)