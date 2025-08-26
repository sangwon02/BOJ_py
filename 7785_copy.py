import sys
input = sys.stdin.readline

n = int(input())
company = {}

for _ in range(n):
    n1, n2 = input().split()

    if n2 == 'enter':
        company[n1] = 'enter'
    else:
        if company[n1]:
            del company[n1]

for i in sorted(company, reverse=True):
    print(i)