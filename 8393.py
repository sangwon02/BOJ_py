x = int(input())
y = 0

if x>=1 and x<=10000:
    for n in range(1, x+1):
        y += n

print(y)