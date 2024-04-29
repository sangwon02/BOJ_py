import sys
input = sys.stdin.readline

n = int(input())  # 손님 수 입력 받음
li = []  # 손님들이 생각한 팁을 넣을 리스트
for i in range(n):  
    tip = int(input())  # 각각 생각한 팁을 받고
    li.append(tip)  # 리스트에 넣음
li.sort(reverse=True)  # 내림차순으로 정렬
realtip = 0
think = 0
for i in range(n):  
    if (li[i] - think) <= 0:  # 만약 생각한 팁에서 등수로 인해 바뀐 값이 음수면
        break  # for문 종료
    realtip +=  li[i] - think  # 강호가 받은 팁에 더해줌
    think += 1  # 등수로 인해 감소하는 값 증가
print(realtip)  # 정답 출력