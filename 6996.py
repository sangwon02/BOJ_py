N = int(input()) #입력 받을 케이스의 수

for i in range(N): #N만큼 반복
    s1, s2 = input().split() #공백을 구분하여 문자형 2개 입력 받음
    li1 = list(s1) #s1을 리스트(l1)에 넣음(문자 하나하나씩)
    li2 = list(s2) #s2을 리스트(l2)에 넣음(문자 하나하나씩)
    li1.sort(reverse=False) #l1을 오름차순으로 정렬
    li2.sort(reverse=False) #l2을 오름차순으로 정렬
    
    if li1 == li2:#만약 두리스트가 같으면 출력
        print(s1, "&", s2, "are anagrams.")
    else: #다르면 출력
        print(s1, "&", s2, "are NOT anagrams.")