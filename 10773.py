K = int(input())
li = []
for i in range(K):
    n = int(input())
    if n != 0:
        li.append(n)
    elif n == 0:
        if len(li)==0:
            continue
        del li[len(li)-1]
print(sum(li))