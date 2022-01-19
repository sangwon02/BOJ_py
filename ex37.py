n = int(input())
num = 0

for i in range(n):
    list1 = list(map(int, input().split()))
    num = sum(list1[1:])/list1[0]
    st = 0
    for j in list1[1:]:
        if j > num:
            st+=1
    rate = st/list1[0] *100
    print(f'{rate:.3f}%')
