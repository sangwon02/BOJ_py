import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n과 m을 입력 받음

arr = []  # 

# n개의 문자열을 arr에 저장
for i in range(n):
    arr.append(input().strip())

cnt = 0  # Hamming Distance의 합을 저장할 변수
result = ''  # Hamming Distance의 합이 가장 작은 DNA를 저장할 변수
for i in range(m):  # result의 길이가 m이여야 하니 m번 반복
    a_cnt,t_cnt, g_cnt, c_cnt = 0, 0, 0, 0  # A, T, G, C가 나오면 카운트 할 변수
    for j in range(n):  # n개의 DNA를 전부 탐색
        # 각 문자가 몇 개 있는지 저장
        if arr[j][i] == 'A': 
            a_cnt += 1
        elif arr[j][i] == 'T':
            t_cnt += 1
        elif arr[j][i] == 'G':
            g_cnt += 1
        elif arr[j][i] == 'C':
            c_cnt += 1
            
    # result에 가장 많이 나온 문자를 저장하고
    # cnt(Hamming Distance)에 가장 많이 나온 문자를 제외한 문자 개수를 더 해줌
    # 여기서 포인트가 A, G, C, T 순이 아닌 알파벳 순서로 if문을 구성해야함
    if max(a_cnt, c_cnt, g_cnt, t_cnt) == a_cnt: 
        result += 'A'  
        cnt += c_cnt + g_cnt +t_cnt  
    elif max(a_cnt, c_cnt, g_cnt, t_cnt) == c_cnt:
        result += 'C'
        cnt += a_cnt + g_cnt +t_cnt
    elif max(a_cnt, c_cnt, g_cnt, t_cnt) == g_cnt:
        result += 'G'
        cnt += a_cnt + c_cnt +t_cnt
    elif max(a_cnt, c_cnt, g_cnt, t_cnt) == t_cnt:
        result += 'T'
        cnt += c_cnt + g_cnt + a_cnt
    
    
# 정답 출력
print(result) 
print(cnt)  