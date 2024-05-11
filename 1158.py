import sys
input = sys.stdin.readline

n,k = map(int,input().split())
num = [i for i in range(1,n+1)]  # 원에 앉아 있는 사람 생성

Josephus = []   # 답을 담을 리스트
cnt = 0  # 제거될 인덱스 번호

for t in range(n):
    cnt += k-1  
    if cnt >= len(num):  # 한바퀴를 돌고 그 다음으로 넘어갈때 
        cnt = cnt%len(num)  # 값을 나머지로 바꿈  

    Josephus.append(str(num.pop(cnt)))  # 제거된 번호를 요세푸스리스트에 저장

# 답 출력
print("<",end="")
for i in range(n):
    if i == (n-1):
        print(Josephus[i], end="")
    else:
        print(Josephus[i],end=", ")
print(">")