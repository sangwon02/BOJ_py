n1, n2 = map(int, input().split())

set1 = {}

for _ in range(n1):
    site, ps = input().split()
    set1[site] = ps

for _ in range(n2):
    print(set1[input().rstrip()])