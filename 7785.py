import sys
input = sys.stdin.readline

n = int(input())
company = {}

for _ in range(n):
    name, paly = input().split()
    if paly == "enter":
        company[name] = True
    else:
        del company[name]

res = sorted(company.keys(), reverse=True)

for name in res:
    print(name)