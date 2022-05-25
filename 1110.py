x = int(input()) #정수를 입력 받음
e = x #정수를 저장함
cnt = 0 #카운트 변수

while True:#무한 반복
    a = e//10 #e의 십의 자리를 구함
    b = e%10 #e의 일의 자리를 구함
    c = (a+b)%10 #a와 b를 더한 값의 일의 자리를 구함
    e = b*10 + c #b를 십의 자리로 하고 c를 일의 자리인 수를 e에 저장
    cnt = cnt + 1 #카운트 +1
    if e == x: #만약 e와 x가 같다면
        break #while문 종료

print(cnt) 