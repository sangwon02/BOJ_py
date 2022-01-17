import sys

x = int(input())

for n in range(1,x+1,1):
    y, z = map(int, sys.stdin.readline().split())
    print("Case #%s: %s + %s = %s" % (n , y, z, y+z))