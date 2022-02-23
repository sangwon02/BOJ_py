x, y = map(int, input().split())
li = list(map(int, input().split()))
num = len(li)

sum = 0
for i in range(0, num):
        for j in range(i + 1, num):
                for k in range(j + 1, num):
                        if li[i] + li[j] + li[k] > y:
                                continue
                        else:
                                sum = max(sum, li[i] + li[j] + li[k])

print(sum)