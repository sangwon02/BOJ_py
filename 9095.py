import sys
input = sys.stdin.readline

t = int(input())

li = [1,2,4]  # n이 1,2,3일때 값

for i in range(t):  # t만큼 반복
    n = int(input())  
    if n > len(li):  # 만약 n이 리스트가 갖고 있는 값보다 크다면
        for j in range(len(li)-1, n-1):  # n값 만큼 추가 
            li.append(li[j-2]+li[j-1]+li[j]) 
            
    print(li[n-1]) # 원하는 답 출력
