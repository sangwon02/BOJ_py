import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
n = int(input())

result = 0

for _ in range(n):
    
    current = 0
    for _ in range(3):
        aNum, bNum, cNum = map(int, input().split())
        current += aNum*a + bNum*b + cNum*c
    
    result = max(result, current)
    
    
print(result)