n = int(input()) #정수를 입력 받음
num1 = 1

while n>num1: #n이 num1보다 크면
    n -= num1 #n은 n-num1을 해주고 
    num1 += 1 #num1에 1을 더해준다

if num1%2==0: #num1이 2로 나누어지면
    a=n #a는 분자 부분
    b=num1-n+1 #b는 분모
    
else: #num1이 2로 나누어지지 않으면
    a=num1-n+1 #a는 분자 부분
    b=n #b는 분모
print(a, '/', b, sep='') #분수 출력