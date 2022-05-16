vowel = ['a','e','i','o','u']#모음을 모아둔 리스트
while 1: #무한 반복
    s = input() #문자열 입력 받음
    if s=='#' : # #이라고 입력하면
        break #종료
    li = [] #비어있는 리스트 생성 
    for i in s: #문자열의 문자들을 리스트에 넣어줌
        li.append(i) 
    #만약 문자열에 모음이 없다면
    if 'a' not in li and 'e' not in li and 'i' not in li and 'o' not in li and 'u' not in li:
        print(s+"ay") #문자열 + ay 출력
    
    else: #아니면
        while li[0] not in vowel : #첫글자가 모음이 일때까지 반복
            li.append(li[0]) #자음을 뒤에 추가하고
            del li[0] #맨앞에 자음 삭제
        for i in li: #리스트의 문자들 출력
            print(i,end='')
        print("ay") #ay출력