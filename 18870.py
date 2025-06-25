import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))  # 좌표 입력 받고

li2 = sorted(list(set(li)))  # 중복된 값을 제거 후 오름차순으로 정렬하고

dic = { li2[i] : i for i in range(len(li2))}  
# 값과 그에 따른 li2의 인덱스를 딕셔너리에 저장: {값: 순위} 형태

for i in li:  # 좌표를 하나씩 돌면서
    print(dic[i], end = ' ')  # 딕셔너리의 값을 출력