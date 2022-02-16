#직각사각형을 만들어야하는데 3점의 좌표만 주어졌다.
#나머지 하나의 좌표를 구하시오.

xli = []
yli = []

for i in range(3):
    x, y = map(int, input().split())
    xli.append(x)
    yli.append(y)
    
for i in range(3):
        if xli.count(xli[i]) == 1:
                x = xli[i]
        if yli.count(yli[i]) == 1:
                y = yli[i]

print(x, y)


