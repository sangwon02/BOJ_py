n = int(input()) #반복할 숫자 입력받음

for i in range(n):#n만큼 반복
    a = int(input()) #숫자 입력 받음
    b = int(str(a)[::-1]) #입력 받은 숫자 뒤집어줌
    c = a + b #a하고 b 더함
    if c == int(str(c)[::-1]): #c와 거꾸로 된 c가 같으면
        print("YES") #YES 출력
    else: #다르면
        print("NO") #NO 출력