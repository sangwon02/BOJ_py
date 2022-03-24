n = int(input())
set1 = set(map(int, input().split()))

li = list(set1)

li.sort(reverse=False)

for i in li:
    print(i, end=" ")