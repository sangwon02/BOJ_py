N = int(input()) #입력 받을 문자의 수

for i in range(N): #N만큼 반복
    s = str(input()) #문자를 입력 받음
    s= s[0].upper()+s[1:] #첫글자를 대문자로 바꿔주고 나머지 글자는 그대로
    print(s) #s를 출력
