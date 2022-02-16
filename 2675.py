n = int(input())

for i in range(n):
    a, b = input().split()
    a = int(a)
    b = str(b)
    num = 0
    for j in b:
        for k in range(a):
            print(b[num:num+1], end = '')
        num += 1
    print('')
