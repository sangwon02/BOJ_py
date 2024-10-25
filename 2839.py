# n = int(input()) #정수 입력 받음
# if n%5==0: #n이 5로 나누어떨어지면
#     print(n//5) #n나누기5 출력
# elif (n-3)%5==0 and n>=3:#n-3이 5로 나누어지고 n이 3이상이면
#     print((n-3)//5+1) #(n-3)//5+1을 출력
# #더이상 주석 달 필요는 없는듯
# elif (n-6)%5==0 and n>=6:
#     print((n-6)//5+2)
# elif (n-9)%5==0 and n>=9:
#     print((n-9)//5+3)
# elif (n-12)%5==0 and n>=12:
#     print((n-12)//5+4)
# else:
#     print(-1)
import sys
input = sys.stdin.readline

sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 : 
        bag += (sugar // 5) 
        print(bag)
        break
    sugar -= 3  
    bag += 1
else:
    print(-1)