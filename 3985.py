L = int(input()) #롤케이크의 길이 입력 받음
li = [0] * (L + 1) #크기가 L+1인 리스트 생성
N = int(input()) #방청객의 인원을 입력 받음
num1 = [0] * (N + 1) #방청객의 인원 만큼 리스트를 생성함
maxnum = 0 #가장 많은 조각을 받을 것으로 기대하고 있던 방청객의 번호
M_cnt = 0 #그 사람의 기대값

for i in range(1, N + 1): #i에 1부터 N+1까지 대입하면서 반복
    P, K = map(int, input().split()) #방청객이 원하는 조각을 입력받음
    if K - P - 1 > M_cnt: #K-P가 기대값보다 크다면
        #가장 많을 조각을 받을 거라고 예상되는 사람을 바꿔줌
        maxnum = i
        M_cnt = K-P-1

    cnt = 0
    for j in range(P, K + 1): #i에 P부터 K+1까지 대입하면서 반복
        if not li[j]:#조각이 아직 있다면
            li[j] = 1 #먹었다고 표시하고
            cnt += 1 #cnt +1해줌
    num1[i] = cnt #방청객이 실제로 받은 양을 리스트에 담아줌

print(maxnum) #가장 많은 조각을 받을 것으로 기대하고 있던 방청객의 번호 출력
print(num1.index(max(num1))) #실제로 가장 많이 받은 사람의 번호