str1 = input()
li = []

for i in str1:
    li.append(int(i))

li.sort(reverse=True)
for i in li:
    print(i,end="")