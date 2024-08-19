import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    li = []
    li = list(map(int, input().split()))
    li.sort(reverse=True)
    print(li[2])