import sys
input = sys.stdin.readline

t = int(input())
# 사실 이 문제는 단순 구현 문제이다.
# 만약 원하는 답이 n이라고 하면 
# 1+(n-1의 합을 나타내는 방법), 2+(n-2의 합을 나타내는 방법), 3+(n-3의 합을 나타내는 방법)
# 이렇게 구하면 n을 1,2,3의 합을 통해 나타내는 방법의 수가 나온다.

li = [1,2,4]  # n이 1,2,3일때 값

for i in range(t):  # t만큼 반복
    n = int(input())  
    if n > len(li): # 만약 n이 리스트의 길이(구하는 방법)보다 큰 경우
        for j in range(len(li)-1, n): # 새롭게 추가해준다.
            li.append(li[j]+li[j-1]+li[j-2])
            
    print(li[n-1]) # 원하는 답 출력
