import sys

x, y = map(int, sys.stdin.readline().split())

while x != 0 and y != 0:
    print(x + y)
    x, y = map(int, sys.stdin.readline().split())