st = input()  # 찾고자 하는 문자열 입력 받음
n = int(input())  # 몇개 비교할건지 입력 받음
cnt = 0

for i in range(n):  # n번 반복
    rings = input()  # 반지의 문자열 입력 받고
    rings = rings*2  # 끝이 연결되어야 하니 반복한 문자열로 바꿔줌

    if st in rings:  # 만약 겹치는 부분이 있다면 
        cnt += 1  # 카운트 해줌

print(cnt)  # 카운트 된게 몇개인지 출력