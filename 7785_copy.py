n = int(input())
li = {}

for _ in range(n):
    n1, n2 = input().split()

    if n2 == 'enter':
        li[n1] = 'enter'
    else:
        if li[n1]:
            del li[n1]

for i in sorted(li, reverse=True):
    print(i)