import sys

while True:
    try:
        x, y = map(int, sys.stdin.readline().split())
    except:
        break
    print(x + y)