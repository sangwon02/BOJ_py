N = int(input())
li = [0]*26
li2 = []

for i in range(N):
    s = input()
    for j in range(97, 123):
        if chr(j) == s[0]:
            li[j-97] += 1
            if li[j-97] == 5:
                li2.append(s[0])

if not li2:
    print("PREDAJA")
else:
    li2.sort(reverse=False)
    for i in li2:
        print(i,end="")
