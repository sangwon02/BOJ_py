str1 = input() #문자입력 받음
cnt = 0 #카운트 해줄 변수
for i in str1: #입력받은 문자열의 문자를 i에 하나씩 대입하면서 반복
    print(i, end ="") #i프린트(줄바꿈 없이)
    cnt += 1 #cnt +1
    if cnt%10==0: #cnt가 10으로 나누어지면
        print(" ") #줄바꿈
