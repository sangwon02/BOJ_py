T = int(input()) #반복할 숫자 입력받음

for i in range(T): #T만큼 반복
    s = input() #문자열을 입력받음
    print(s[0]+s[-1]) #문자열의 첫번째 문자와 마지막 문자를 출력한다.