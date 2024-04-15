import sys
input = sys.stdin.readline

while True:  # 무한 반복
    ss = input().rstrip()  # 문자열 입력 받고
    if not ss:  # 입력 받은게 없다면 무한 반복 종료
        break
    s, t = ss.split()  # 띄어쓰기 기준으로 나누어주고
    cnt = 0  # 몇 개의 알파벳이 맞는지 카운트 할 변수
    check = True  # 문자열을 비교할 반복문 사용시 활용
    i = 0  # t의 알파벳 순서대로 비교
    while check:  # check가 True일 때 무한 반복 
        if t[i] == s[cnt]: # 만약 t의 i번째 알파벳과 s의 cnt번째 알파벳이 같다면
            cnt += 1  #다음 s의 알파벳으로 넘어감
        if cnt == len(s):  # 만약 부분 문자열이라면
            print("Yes")  # 출력 후
            check = False  # 종료
        else: 
            i += 1  # t의 다음 알파벳으로 넘어가 비교하고 
            if i == len(t):  # 만약 t를 전부 돌았다면 
                check = False  # 비교 종료

    if cnt != len(s):  # 만약 부분 문자열이 아닐 때 
        print("No")