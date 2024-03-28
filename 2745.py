s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
     
N, B = input().split()

N = N[::-1]

result = 0

for i, num in enumerate(N):
    result += ((int(B)**i) * (s.index(num)))
print(result)