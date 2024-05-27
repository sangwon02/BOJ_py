import sys
input = sys.stdin.readline

n = int(input())
li1 = list(map(int, input().split()))
m = int(input())
li2 = list(map(int, input().split()))

n_dic = {}

for i in li1:  # 상근이 가진 카드의 수를 돌며
    if i in n_dic: # 만약 딕셔너리에 있다면
        n_dic[i] += 1  # 카드의 수를 키값으로 하고 value값을 1올려줌
    else:  # 만약 없다면
        n_dic[i] = 1  # 카드의 수를 키값으로 하며 value 1로 저장

for i in li2:  # 비교할 수를 돌며
    if i in n_dic:  # 만약 딕셔너리에 있다면 
        print(n_dic[i], end=' ')  # 그 값의 value값을 출력
    else:  # 없다면
        print(0, end=' ')  # 0출력