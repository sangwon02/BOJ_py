N = int(input())
book = {}

for i in range(N):
    s = input()
    if s in book:
        book[s] += 1
    else:
        book[s] = 1

li = []
for s in book:
    li.append((s, book[s]))

li.sort(key=lambda  x:(-x[1], x[0]))
print(li[0][0])