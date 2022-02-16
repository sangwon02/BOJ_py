def han(a):
    li = []
    cnt = 0
    for i in range(1, a+1):
        list1 = list(map(int, str(i)))
        if i <100:
            cnt += 1
        elif list1[0] - list1[1]== list1[1]-list1[2]:
            cnt += 1
    return cnt
        

a = int(input())
print(han(a))