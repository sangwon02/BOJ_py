a, b, c = map(int, input().split())
num = 0 
x = 1

if c > b:
    print(int(a/(c-b)+1))
else:
    print(-1)
 