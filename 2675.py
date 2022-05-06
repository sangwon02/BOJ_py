n = int(input()) #입력받을 문자 수

for i in range(n): #n만큼 반복
    a, b = input().split() #a에는 반복 횟수, b에는 문자를 입력 받고
    a = int(a) #a는 정수형
    b = str(b) #b는 문자열로 바꿈
    num = 0
    for j in b: #b의 문자열 만큼 반복
        for k in range(a): #a만큼 반복
            print(b[num], end = '') #문자열 b의 num번째 문자를 출력
        num += 1 #num += 1
    print('')#줄바꿈 출력
