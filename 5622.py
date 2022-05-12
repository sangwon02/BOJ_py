st = input().upper() #문자열을 입력받음
sum = 0 #시간의 합
for i in st: #문자열의 문자를 순서대로 i에 대입 후 밑 실행
    if i == 'B'or i == 'C'or i == 'A': #i가 B,C,A이면
        sum +=3 #3을 sum에 더함
    elif i == 'E'or i == 'F'or i == 'D':#i가 E,F,D이면
        sum +=4 #4을 sum에 더함
    elif i == 'H'or i == 'I'or i == 'G':#i가 H,I,G이면
        sum +=5 #5을 sum에 더함
    elif i == 'K'or i == 'J'or i == 'L':#i가 K,J,L이면
        sum +=6 #6을 sum에 더함
    elif i == 'N'or i == 'O'or i == 'M':#i가 N,Q,M이면
        sum +=7 #7을 sum에 더함
    elif i == 'Q'or i == 'S'or i == 'R'or i == 'P':#i기 Q,S,R이면
        sum +=8 #8을 sum에 더함
    elif i == 'U'or i == 'V'or i == 'T':#i가 U,V,T이면
        sum +=9 #9을 sum에 더함
    elif i == 'X'or i == 'Y'or i == 'W'or i == 'Z':#i가 X,Y,W,Z이면
        sum +=10 #10을 sum에 더함
    else:#나머지 경우면
        sum +=11 #11을 sum에 더함
print(sum) #sum을 출력
