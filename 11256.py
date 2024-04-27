import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    box = []  # 박스의 크기를 넣을 리스트
    boxcnt = 0  # 필요한 박스
    num = 0  # 필요한 박스만큼 들어갈 수 있는 사탕 개수
    
    j, n = map(int, input().split())
    for k in range(n):
        r, c = map(int, input().split())  # 상자의 크기를 저장해줌
        box.append(r*c)
    box.sort(reverse=True)  # 상자의 크기 오름차순으로 정렬
    while num < j:  # 필요한 박스만큼 들어갈 수 있는 사탕 개수가 사탕보다 많으면 종료
        num += box[boxcnt]  # 남아있는 상자중에 가장 큰 상자를 선택함
        boxcnt += 1  # 사용한 상자의 개수 +1
    
    print(boxcnt)  # 필요한 상자의 개수 출력
    