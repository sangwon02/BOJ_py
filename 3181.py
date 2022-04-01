li = input().split()
li2 = []

li2.append(li[0].upper())

for i in range(1, len(li), 1):
    if  li[i] == 'i' or  li[i] == 'pa' or  li[i] == 'te' or  li[i] == 'ni' or  li[i] == 'niti' or  li[i] == 'a' or li[i] == 'ali' or li[i] == 'nego' or li[i] == 'no' or li[i] == 'ili':
        continue
    else:
        li2.append(li[i].upper())
 
for i in li2:
    print(i[0],end="")