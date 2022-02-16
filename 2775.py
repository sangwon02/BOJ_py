n = int(input())

for i in range(n):
    num = []
    a = int(input())
    b = int(input())
    num = [j for j in range(1, b+1)]

    for l in range(a):
        for j2 in range(1, b):
            num[j2] += num[j2-1]
    print(num[b-1])