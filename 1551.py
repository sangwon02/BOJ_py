n1, n2 = map(int, input().split()) #n1은 수열의 크기, 행위를 n2번 함  
A = list(map(int, input().split(","))) #리스트 입력 받음
cnt = 1

for k in range(n2): 
    for i in range(n1-cnt): #n1(배열의 크기) - cnt(1에서 한번할때마다 1증가)
        a = A[i] #a에 i번째 리스트 값을 저장해주고
        A[i]=A[i+1]-a #i번째 리스트를 A[i+1]-a로 바꿔줌
    cnt += 1

for j in range(n1-n2): #리스트의 크기는 n1-n2
    print(A[j], end="") #리스트 출력
    if j<n1-n2-1:
        print(",",end="")