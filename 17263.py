n = int(input())

li = list(map(int, input().split()))

li.sort(reverse=False)

print(li[n-1])