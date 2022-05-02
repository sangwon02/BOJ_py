N = int(input())
li = [0]*26
li2 = []

for i in range(N): #N의 개수만큼 이름을 입력받음
    s = input()
    for j in range(97, 123):
        if chr(j) == s[0]: #입력받은 이름의 첫글자가 소문자이면
            li[j-97] += 1 #소문자의 자리에 1늘려준다.
            if li[j-97] == 5: #만약 소문자가 같은 이름이 5명이면
                li2.append(s[0])#입력받은 이름의 첫글자를 li2에 저장한다.

if not li2: #li2가 비어있다면
    print("PREDAJA") #기권
else:
    li2.sort(reverse=False)#오름차순으로 정리하고
    for i in li2: #리스트 내용 출력
        print(i,end="")
