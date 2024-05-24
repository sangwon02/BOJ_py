import sys
input = sys.stdin.readline

n = input().strip()
length = len(n) - 1
result = 0

for i in range(length): # 가장 높은 자릿수의 직전까지의 합을 구하고
    result += 9*(10**i)*(i+1)
# 가장 높은 자릿수의 합을 구한다.
result += ((int(n)-(10**length))+1)*(length+1)
    
print(result)