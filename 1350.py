N = int(input()) #파일의 개수
li = list(map(int, input().split())) #파일의 크기
scale = int(input()) #클러스터의 크기
sum1 = 0

for i in range(N): #파일의 개수만큼 반복
    if li[i]==0:
        continue
    n1 = li[i]//scale #사용되는 클러스터의 개수
    if li[i]%scale: #나누어떨어지지 않으면
        n1 += 1 #사용되는 클러스터의 개수 +1
    sum1 += scale*n1 #사용한 디스크 공간
    
print(sum1) #사용한 디스크 공간 출력