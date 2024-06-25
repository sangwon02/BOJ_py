import sys
input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    arrival, check = map(int, input().split())  # 소들의 도착 시간과 검문 시간을
    li.append([arrival, check])  # 리스트에 저장
li.sort(reverse=False)  # 리스트를 오름차순으로 정렬
time = 0  # 총 경과 시간
for i in li:
    if time < i[0]:  # 만약 소가 도착한 시간이 경과 시간보다 늦게 도착했다면
        time = i[0] + i[1]  # 경과 시간을 소의 (도착 시간 + 검문 시간)으로 바꾸어줌
    elif time >= i[0]:  # 만약 소가 도착한 시간이 경과 시간보다 같거나 빠르다면
        time += i[1]  # 다른 소들이 검문이 끝난 후 검문 시간을 가짐
print(time)  # 총 경과 시간 출력