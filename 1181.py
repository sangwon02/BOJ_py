n = int(input())
li = []

for i in range(n):
    li.append(input())

st = set(li) 
li = list(st) 
li.sort(reverse=False)    
li.sort(key=len)


for i in li:
    print(i)