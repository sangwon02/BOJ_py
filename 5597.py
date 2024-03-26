li = []

for i in range(30):
    li.append(i+1)
    
for i in range(28):
    n = int(input())
    li.remove(n)

for i in li:
    print(i)
