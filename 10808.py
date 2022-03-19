S = input()
li = [0]*26

for i in S:
    li[ord(i) - 97] += 1
    #아스키코드를 사용
    
for j in li:
    print(j, end=" ")
