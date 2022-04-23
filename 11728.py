n1, n2 = map(int, input().split())

li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

result = li1 + li2
result.sort()

for i in result:
    print(i, end=" ")