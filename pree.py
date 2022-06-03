x = int(input()) #정수를 입력 받음
e = x #정수를 저장함
f = 0 

a = e//10 #e를 10으로 나누었을 때 몫을 구함
print(a)
b = e%10 #e를 10으로 나누었을 때 나머지를 구함
print(b)
c = (a+b)%10 #a와 b를 더하고 
print(c)

for i in range(10): #i에 0부터 9까지 대입하면서 반복