import sys
input = sys.stdin.readline

r, c = map(int, input().split())  # 이미지 크기를 입력 받음

li = []

for i in range(r):  # 이미지의 픽셀 입력 받음
    li1 = list(map(int, input().split()))
    li.append(li1)
    
t = int(input())
final = []  # 필터링된 픽셀의 값을 넣을 리스트

for i in range(r-2):  # 3칸씩 넣을 거니 -2 해줌
    for j in range(c-2):
        li1 = []
        for k in range(3):  # i와 j 기준으로 3칸 범위를 탐색
            for o in range(3):
                li1.append(li[i+k][j+o])  # 각 값을 리스트에 넣어주고
        li1.sort(reverse=False)  # 오름차순으로 정렬 후
        final.append(li1[4])  # 필터링된 픽셀의 값을 최종 리스트에 넣어줌
cnt = 0 
for i in final:  # 최종값을 하나하나 돌면서 확인
    if i >= t :  # 만약 t 이상이라면
        cnt += 1  # +1

print(cnt)  # 답 출력