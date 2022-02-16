n = int(input())
list1 = list(map(int, input().split()))
list2 = []
num = 0
mscore = max(list1)
for i in list1:
    list2.append((i/mscore)*100)
for i in list2:
    num = num+i
print(num/n)