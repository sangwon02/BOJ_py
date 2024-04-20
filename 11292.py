import sys
input = sys.stdin.readline

while True:
    n = int(input())  # 입력 받을 학생 수
    if n == 0:  # 0이면 종료
        break
    name = []  # 이름을 넣을 리스트
    height = []  # 키를 넣을 리스트
    for i in range(n):
        n, h = input().split()  # 이름과 키를 입력 받고
        name.append(n)  # 따로 저장
        height.append(float(h))
    m = max(height)  # 가장 큰 키를 찾고
    # 가장 큰 키들이 있는 인덱스를 찾아서 anwer리스트에 넣고
    answer = [index + 1 for index, val in enumerate(height) if val == m]  
    
    for i in answer:  # 이름들이 있는 리스트에서 인덱스를 사용해 출력
        print(name[i-1], end=" ")
    print("")