n = int(input())

li =[]
for i in range(n):
    li.append(int(input()))
li.sort(reverse=False)

for i in li:
    print(i)