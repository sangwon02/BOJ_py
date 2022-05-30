D = {} #딕셔너리 생성
for i in range(10): #i에 0부터 9까지 대입하면서 반복
    D[i] = str(i) #i(정수):i(문자형)을 저장함
for i in range(26): #i에 0부터 25까지 대입하면서 반복
    D[i+10] = chr(65+i)#i+10(정수):i의 따른 아스키 코드 값(문자형)을 저장함

n, b = map(int,input().split()) #공백을 구분하여 정수 2개를 입력 받음
ans = [] #리스트 생성
while 1: #무한 반복
    if n == 0: break #n이 0이면 종료
    x = n % b #x는 n나누기b의 나머지
    ans.append(D[x])#리스트에 x의 딕셔너리 값을 추가
    n //= b #n은 b의 나눴을때 몫
print(''.join(ans[::-1])) #ans를 역순으로 출력