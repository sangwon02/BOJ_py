N, K = map(int, input().split())

li = list(map(int, input().split(",")))

for _ in range(K):
    new_li = []
    for i in range(len(li) - 1):
        new_li.append(li[i+1] - li[i])
    li = new_li  

print(",".join(map(str, li)))