import sys
input = sys.stdin.readline

n = int(input())

li = [0, 1]
i = 1
while len(li) <= n:
    li.append(li[i] + li[i-1])
    i+=1
print(li[n])