cnt=1 #카운트할 변수
while True: #무한 반복
    n1,s,n2=input().strip().split()#띄어쓰기를 기준으로 3개의 문자를 입력받음
    if s=="E": #s가 E이면
        break #종료
    #각각의 식이 맞는지 아닌지 확인한다.
    #만약 아니라면 false출력 맞다면 true출력
    if s=="!=": 
        #format(cnt)는 {}에 넣어줌
        print("Case {}: ".format(cnt)+str(int(n1)!=int(n2)).lower())
    elif s=="<":
        print("Case {}: ".format(cnt)+str(int(n1)<int(n2)).lower())
    elif s=="<=":
        print("Case {}: ".format(cnt)+str(int(n1)<=int(n2)).lower())
    elif s==">":
        print("Case {}: ".format(cnt)+str(int(n1)>int(n2)).lower())
    elif s==">=":
        print("Case {}: ".format(cnt)+str(int(n1)>=int(n2)).lower())
    elif s=="==":
        print("Case {}: ".format(cnt)+str(int(n1)==int(n2)).lower())
    cnt+=1 #cnt에 1를 더해줌