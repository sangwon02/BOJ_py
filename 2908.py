import sys

x, y = map(int, sys.stdin.readline().split()) #세자리 정수 2개를 입력받음

num1 = x//100 + ((x%100)//10)*10 + (x%10)*100 #정수를 거꾸로 바꾸어줌
num2 = y//100 + ((y%100)//10)*10 + (y%10)*100 

#더 큰수를 출력해줌
if num1>num2: 
    print(num1)
else:
    print(num2)

    