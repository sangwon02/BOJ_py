import sys

x = int(input())

for _ in range(x):
    y, z = map(int, sys.stdin.readline().split())
    print(y+z)