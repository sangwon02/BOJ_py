import sys #sys 불러옴

while True: #무한 반복
    str1 = sys.stdin.readline().rstrip('\n') #문자열을 입력 받음

    if not str1: #문자열이 아니면
        break #중지

    n1, n2, n3, n4 = 0, 0, 0, 0 #변수 4개 생성
    for i in str1: #문자열의 문자를 차례로 i에 대입하면서 반복
        if i.islower(): #i가 소문자면
            n1 += 1#n1 +1
        elif i.isupper():#i가 대문자면
            n2 += 1#n2 +1
        elif i.isdigit():#i가 숫자면
            n3 += 1#n3 +1
        elif i.isspace():#i가 공백이면
            n4 += 1#n4 +1
    print(n1, n2, n3, n4) #출력